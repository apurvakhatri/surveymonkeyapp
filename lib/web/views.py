import json
from django.http import HttpResponse
from django.shortcuts import render
from yellowant import YellowAnt
from ..records.models import YellowUserToken, SurveyMonkeyUserToken
from django.conf import settings


def index(request, path=""):
    print("in index")
    context = {
        "user_integrations": []
    }
    if request.user.is_authenticated:
        user_integrations = YellowUserToken.objects.filter(user=request.user.id)
        # for user_integration in user_integrations:
        #     print(user_integration)
        #     context["user_integrations"].append(user_integration)
    context = {"base_href": settings.BASE_HREF,
               "application_id": settings.YA_APP_ID,
               }

    print("returning from index")
    return render(request, "home.html", context)


def userdetails(request):
    print("in userdetails")
    user_integrations_list = []
    if request.user.is_authenticated:
        user_integrations = YellowUserToken.objects.filter(user=request.user.id)
        for user_integration in user_integrations:
            print(user_integration)
            try:
                smut = SurveyMonkeyUserToken.objects.get(user_integration=user_integration)

                user_integrations_list.append({\
                "user_invoke_name":user_integration.yellowant_integration_invoke_name,\
                "id":user_integration.id, "app_authenticated":True\
                })

            except SurveyMonkeyUserToken.DoesNotExist:
                user_integrations_list.append({\
                "user_invoke_name":user_integration.yellowant_integration_invoke_name,\
                "id":user_integration.id, "app_authenticated":False\
                })
    print("returning")
    return HttpResponse(json.dumps(user_integrations_list), content_type="application/json")

def delete_integration(request, integrationId=None):
    print("In delete_integration")
    print(integrationId)
    access_token_dict = YellowUserToken.objects.get(id=integrationId)

    access_token = access_token_dict.yellowant_token
    user_integration_id = access_token_dict.yellowant_integration_id
    print(user_integration_id)

    url = "https://api.yellowant.com/api/user/integration/%s"%(user_integration_id)
    yellowant_user = YellowAnt(access_token=access_token)
    profile = yellowant_user.delete_user_integration(id=user_integration_id)
    response_json = YellowUserToken.objects.get(yellowant_token=access_token).delete()
    print(response_json)

    return HttpResponse("successResponse", status=204)
