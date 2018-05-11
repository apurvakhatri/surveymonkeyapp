from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from yellowant import YellowAnt
import requests
import json, uuid
from yellowant.messageformat import MessageClass, MessageAttachmentsClass, MessageButtonsClass, AttachmentFieldsClass
import traceback
from django.views.decorators.csrf import csrf_exempt
from records.models import YellowUserToken, YellowAntRedirectState, AppRedirectState, SurveyMonkeyUserToken
from records.YellowAntCommandCenter import CommandCenter
from django.contrib.auth.models import User

SM_API_BASE = settings.SM_API_BASE
ACCESS_TOKEN_ENDPOINT = "/oauth/token"
USER_INFO_ENDPOINT = "/v3/users/me"
# Create your views here.

def redirectToYellowAntAuthenticationPage(request):
    user = User.objects.get(id=request.user.id)
    state = str(uuid.uuid4())
    YellowAntRedirectState.objects.create(user = user, state = state)
    return HttpResponseRedirect("{}?state={}&client_id={}&response_type=code&redirect_url={}".format(settings.YELLOWANT_OAUTH_URL, state, settings.YELLOWANT_CLIENT_ID,settings.YELLOWANT_REDIRECT_URL))


def yellowantRedirecturl(request):
    #print('It is here')
    code = request.GET.get('code')
    #print(code)
    state = request.GET.get("state")
    yellowant_redirect_state = YellowAntRedirectState.objects.get(state = state)
    user = yellowant_redirect_state.user

    y = YellowAnt(app_key = settings.YELLOWANT_CLIENT_ID, app_secret= settings.YELLOWANT_CLIENT_SECRET, access_token=None,
    redirect_uri=settings.YELLOWANT_REDIRECT_URL)
    #access_token_dict is json structured
    access_token_dict = y.get_access_token(code)
    access_token = access_token_dict['access_token']
    yellowant_user = YellowAnt(access_token=access_token)
    profile = yellowant_user.get_user_profile()
    user_integration = yellowant_user.create_user_integration()
    hash_str = str(uuid.uuid4()).replace("-","")[:25]

    ut = YellowUserToken.objects.create(user = user, yellowant_token = access_token, yellowant_id = profile['id'], yellowant_intergration_id = user_integration['user_application'], webhook_id=hash_str)
    state = str(uuid.uuid4())
    AppRedirectState.objects.create(user_integration = ut, state = state)

    url = ('{}?state={}&response_type=code&client_id={}&redirect_uri={}'.format(settings.SURVEYMONKEY_OUTH_URL, state, settings.SURVEYMONKEY_CLIENT_ID,settings.SURVEYMONKEY_REDIRECT_URL))
    return HttpResponseRedirect(url)


def surveymonkeyRedirecturl(request):
    code = request.GET.get("code", False)
    state = request.GET.get("state")
    surveymonkey_redirect_state = AppRedirectState.objects.get(state = state)
    ut = surveymonkey_redirect_state.user_integration

    if code is False:
        return HttpResponse("Invalid Response")
    else:
        data = {
            "client_secret": settings.SURVEYMONKEY_CLIENT_SECRET,
            "code": code,
            "redirect_uri": settings.SURVEYMONKEY_REDIRECT_URL,
            "client_id": settings.SURVEYMONKEY_CLIENT_ID,
            "grant_type": "authorization_code"
        }


        access_token_uri = (SM_API_BASE + ACCESS_TOKEN_ENDPOINT)

        access_token_response = requests.post(access_token_uri, data=data)
        access_json = access_token_response.json()
        #print(access_json)
        access_token = access_json['access_token']
        #print(access_token)
        sut = SurveyMonkeyUserToken.objects.create(user_integration = ut, surveymonkey_access_token = access_token)

        headers = {
            "Authorization" :"Bearer %s" %(access_token) ,
            "Content-Type": "application/json"
        }

        url = (SM_API_BASE + "/v3/surveys")
        response = requests.get(url, headers = headers)
        response_json = response.json()
        surveys_data = response_json["data"]

        surveys_to_enable = [survey['id'] for survey in surveys_data]

        data = {
        "name": "My Webhook",
	    "event_type": "response_completed",
	    "object_type": "survey",
	    "object_ids": surveys_to_enable,
	    "subscription_url": "http://38f456dc.ngrok.io/webhook_receiver/webhook_receiver/%s/"%(ut.webhook_id)
        }

        url = "https://api.surveymonkey.com/v3/webhooks"
        response = requests.post(url, headers = headers, json = (data))
        response_json = response.json()
        print(response_json)

        return HttpResponse("User is Authenticated")

@csrf_exempt
def responsewebhook(request, hash_str=""):
    try:
        yaObj = YellowUserToken.objects.get(webhook_id=hash_str)
    except YellowUserToken.DoesNotExist:
        return HttpResponse("Not Authorized", status=403)


    try:
        dataObj = json.loads(request.body)
        print (dataObj)
        notification_type = dataObj['event_type']
        if notification_type == "response_completed":
            message = MessageClass()
            message.message_text = "New survey response completed"
            message.data = dataObj
            yellowant_user_integration_object = YellowAnt(access_token=yaObj.yellowant_token)
            send_message = yellowant_user_integration_object.create_webhook_message(requester_application = yaObj.yellowant_intergration_id, webhook_name = "response_completed",**message.get_dict())

        return HttpResponse("webhook_receiver/webhook_receiver/")
    except Exception as e:
        print(str(e))
        return HttpResponse("Empty body")

@csrf_exempt
def yellowant_api(request):
    try:
        data = json.loads(request.POST['data'])
        verification_token = data["verification_token"]
        if verification_token == settings.YELLOWANT_VERIFICATION_TOKEN:
            print("Token verified and command is sent")
            cc = CommandCenter(data["user"], data["application"], data["function_name"], data["args"])
            print("Sent")
            return HttpResponse(cc.parse())
        else:
            return HttpResponse(status = 403)
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        return("Something returned")
