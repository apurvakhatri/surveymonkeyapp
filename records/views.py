""" The main views of the "surveymonkeyapp" django project.
It contains YA, SM, Webhooks and yellowant_api views"""
import uuid
import json
import traceback
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from yellowant import YellowAnt
from yellowant.messageformat import MessageClass, MessageAttachmentsClass, \
MessageButtonsClass, AttachmentFieldsClass
from records.models import YellowUserToken, YellowAntRedirectState, AppRedirectState, \
SurveyMonkeyUserToken
from records.YellowAntCommandCenter import CommandCenter


SM_API_BASE = settings.SM_API_BASE
ACCESS_TOKEN_ENDPOINT = "/oauth/token"
USER_INFO_ENDPOINT = "/v3/users/me"


def request_yellowant_oauth_code(request):
    """Initiate the creation of a new user integration on YA
    YA uses oauth2 as its authorization framework.
    This method requests for an oauth2 code from YA to start creating a
    new user integration for this application on YA.
    """
    # get the user requesting to create a new YA integration
    user = User.objects.get(id=request.user.id)
    # generate a unique ID to identify the user when YA returns an oauth2 code
    state = str(uuid.uuid4())
    # save the relation between user and state so that
    # we can identify the user when YA returns the oauth2 code
    YellowAntRedirectState.objects.create(user=user, state=state)
    """Redirect the application user to the YA authentication page.
    Note that we are passing state, this app's client id,
    oauth response type as code, and the url to return the oauth2 code at.
    """ #pylint: disable=pointless-string-statement
    return HttpResponseRedirect("{}?state={}&client_id={}&response_type=code&redirect_url={}"\
    .format(settings.YELLOWANT_OAUTH_URL, state, settings.YELLOWANT_CLIENT_ID, \
    settings.YELLOWANT_REDIRECT_URL))

@csrf_exempt
def yellowant_redirecturl(request):
    """Receive the oauth2 code from YA to generate a new user integration

    This method calls utilizes the YA Python SDK to create a new user
    integration on YA.
    This method only provides the code for creating a new user integration on YA.
    Beyond that, you might need to
    authenticate the user on the actual application (whose APIs this application
    will be calling) and store a relation
    between these user auth details and the YA user integration.
    """
    print("In yellowant_redirecturl")

    # oauth2 code from YA, passed as GET params in the url
    code = request.GET.get('code')

    # the unique string to identify the user for which we will create an integration
    state = request.GET.get("state")

    yellowant_redirect_state = YellowAntRedirectState.objects.get(state=state)
    user = yellowant_redirect_state.user

    # initialize the YA SDK client with your application credentials
    ya_client = YellowAnt(app_key=settings.YELLOWANT_CLIENT_ID,\
    app_secret=settings.YELLOWANT_CLIENT_SECRET, access_token=None,\
    redirect_uri=settings.YELLOWANT_REDIRECT_URL)

    # access_token_dict is json structured
    # get the access token for a user integration from YA against the code
    access_token_dict = ya_client.get_access_token(code)
    access_token = access_token_dict['access_token']

    # reinitialize the YA SDK client with the user integration access token
    yellowant_user = YellowAnt(access_token=access_token)

    # get YA user details
    profile = yellowant_user.get_user_profile()

    # create a new user integration for your application
    user_integration = yellowant_user.create_user_integration()
    hash_str = str(uuid.uuid4()).replace("-", "")[:25]

    # save the YA user integration details in your database
    u_t = YellowUserToken.objects.create(\
    user=user,\
    yellowant_token=access_token,\
    yellowant_id=profile['id'],\
    yellowant_integration_invoke_name=user_integration["user_invoke_name"],\
    yellowant_intergration_id=user_integration['user_application'],\
    webhook_id=hash_str)

    """A new YA user integration has been created and the details have been successfully saved in
    your application's database. However, we have only created an integration on YA.
    As a developer, you need to begin an authentication process for the actual application,
    whose API this application is connecting to. Once, the authentication process for the actual
    application is completed with the user, you need to create a db entry which relates the YA user
    integration, we just created, with the actual application authentication details of the user.
    This application will then be able to identify the actual application accounts corresponding\
    to each YA user integration.""" #pylint: disable=pointless-string-statement

    return HttpResponseRedirect("/integrate_app?id={}".format(str(u_t.id)))




def integrate_app_account(request):
    """ The above function is redirected to this function. It extracts the client idea
    and redirects to SM"""
    print("In integrate_app_account")
    ut_id = request.GET.get("id")
    print(ut_id)

    # Get the user integration.
    u_t = YellowUserToken.objects.get(id=ut_id)
    state = str(uuid.uuid4())
    AppRedirectState.objects.create(user_integration=u_t, state=state)

    url = ('{}?state={}&response_type=code&client_id={}&redirect_uri={}'.\
    format(settings.SURVEYMONKEY_OUTH_URL, state, settings.SURVEYMONKEY_CLIENT_ID,\
    settings.SURVEYMONKEY_REDIRECT_URL))
    print("exiting yellowant_redirecturl")

    return HttpResponseRedirect(url)

def sm_redirecturl(request):
    """This function is for integration of SurveyMonkey application"""
    print("In sm_redirecturl")
    code = request.GET.get("code", False)

    # the unique string to identify the user for which we will create an integration
    state = request.GET.get("state")
    print(state)
    surveymonkey_redirect_state = AppRedirectState.objects.get(state=state)

    u_t = surveymonkey_redirect_state.user_integration

    if code is False:
        return HttpResponse("Invalid Response")
    else:
        # The data to be sent to surveymonkey for SM application authentication.
        data = {
            "client_secret": settings.SURVEYMONKEY_CLIENT_SECRET,
            "code": code,
            "redirect_uri": settings.SURVEYMONKEY_REDIRECT_URL,
            "client_id": settings.SURVEYMONKEY_CLIENT_ID,
            "grant_type": "authorization_code"
        }

        # Url to which request is to be sent for SM access_token.
        access_token_uri = (SM_API_BASE + ACCESS_TOKEN_ENDPOINT)

        access_token_response = requests.post(access_token_uri, data=data)
        access_json = access_token_response.json()
        #print(access_json)
        access_token = access_json['access_token']
        #print(access_token)

        # Inserting the SM application detailself.
        # SM access token is stored against the YA user.
        SurveyMonkeyUserToken.objects.create(user_integration=u_t, \
        surveymonkey_access_token=access_token)

        headers = {
            "Authorization" :"Bearer %s" %(access_token),
            "Content-Type": "application/json"
        }


        """The code below is for webhooks, to enable webhooks for all the surveys available
        as soon as the user is authenticated by SM.
        """ #pylint: disable=pointless-string-statement
        url = (SM_API_BASE + "/v3/surveys")
        response = requests.get(url, headers=headers)
        response_json = response.json()
        surveys_data = response_json["data"]

        surveys_to_enable = [survey['id'] for survey in surveys_data]

        data = {\
        "name":"My Webhook",\
	    "event_type": "response_completed",\
	    "object_type": "survey",\
	    "object_ids": surveys_to_enable,\
	    "subscription_url": "{}/webhook_receiver/webhook_receiver/{}/"\
        .format(settings.BASE_URL, u_t.webhook_id)\
        }

        url = "https://api.surveymonkey.com/v3/webhooks"
        response = requests.post(url, headers=headers, json=(data))
        response_json = response.json()
        print(response_json)

        return HttpResponseRedirect("/")

@csrf_exempt
def responsewebhook(request, hash_str=""):
    """Whenever a new response is completed the user gets notified"""
    try:
        ya_obj = YellowUserToken.objects.get(webhook_id=hash_str)
    except YellowUserToken.DoesNotExist:
        return HttpResponse("Not Authorized", status=403)


    try:
        data_obj = json.loads(request.body)
        print(data_obj)
        notification_type = data_obj['event_type']
        if notification_type == "response_completed":
            message = MessageClass()
            message.message_text = "New survey response completed"
            message.data = data_obj
            yauser_integration_object = YellowAnt(access_token=ya_obj.yellowant_token)

            send_message = yauser_integration_object.create_webhook_message(\
            requester_application=ya_obj.yellowant_intergration_id, \
            webhook_name="response_completed", **message.get_dict())

        return HttpResponse("webhook_receiver/webhook_receiver/")
    except Exception as e:
        print(str(e))
        return HttpResponse("Empty body")

@csrf_exempt
def yellowant_api(request):
    """Receive user commands from YA"""
    print("In yellowant_api")

    try:
        data = json.loads(request.POST['data'])
        verification_token = data["verification_token"]
        print("args are:")
        print(data["args"])
        # verify whether the request is genuinely from YA with the help of the verification token

        if verification_token == settings.YELLOWANT_VERIFICATION_TOKEN:
            print("Token verified and command is sent")

            c_c = CommandCenter(data["user"], data["application"],\
            data["function_name"], data["args"])

            print("Sent")
            return HttpResponse(c_c.parse())
        else:
            return HttpResponse(status=403)
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        return "Something returned"
