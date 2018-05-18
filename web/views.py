from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from records.models import YellowUserToken, SurveyMonkeyUserToken, AppRedirectState
import json
import requests
import traceback
from yellowant import YellowAnt
def index(request):
    print("in index")
    context = {
        "user_integrations": []
    }
    if request.user.is_authenticated:
        user_integrations = YellowUserToken.objects.filter(user=request.user)
        for user_integration in user_integrations:
            print(user_integration)
            context["user_integrations"].append(user_integration)
    return render(request, "home.html", context)


def userdetails(request):
    print("in userdetails")
    user_integrations_list = []
    if request.user.is_authenticated:
        user_integrations = YellowUserToken.objects.filter(user=request.user)
        for user_integration in user_integrations:
            try:
                smut = SurveyMonkeyUserToken.objects.get(user_integration=user_integration)
                user_integrations_list.append({"user_invoke_name":user_integration.yellowant_integration_invoke_name, "id":user_integration.id, "app_authenticated":True})
            except SurveyMonkeyUserToken.DoesNotExist:
                user_integrations_list.append({"user_invoke_name":user_integration.yellowant_integration_invoke_name, "id":user_integration.id, "app_authenticated":False})
    return HttpResponse(json.dumps(user_integrations_list), content_type="application/json")

def delete_integration(request, integrationId=None):
    print("In delete_integration")
    print(integrationId)
    access_token_dict = YellowUserToken.objects.get(id=integrationId)

    access_token = access_token_dict.yellowant_token
    user_integration_id = access_token_dict.yellowant_intergration_id
    print(user_integration_id)

    url = "https://api.yellowant.com/api/user/integration/%s"%(user_integration_id)
    yellowant_user = YellowAnt(access_token=access_token)
    profile = yellowant_user.delete_user_integration(id=user_integration_id)
    response_json = YellowUserToken.objects.get(yellowant_token = access_token ).delete()
    print(response_json)

    return HttpResponse("successResponse", status=204)

def stateDetails(request, id=None):
    print("In stateDetails")
    print(id)
    app_redirect_details = yellowantredirectstate.objects.get(user = id)
    state = app_redirect_details.state
    print(state)
