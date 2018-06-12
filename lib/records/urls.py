from django.urls import path
from django.conf.urls import include
from .views import sm_redirecturl, request_yellowant_oauth_code , yellowant_redirecturl, yellowant_api, responsewebhook
from django.conf.urls import url

urlpatterns = [
    path("create-new-integration/", request_yellowant_oauth_code, name="surveymonkey-auth-redirect"),
    path("redirecturl/", sm_redirecturl, name="surveymonkey-auth-redirect"),
    path("yellowant_redirecturl/", yellowant_redirecturl, name="yellowant-auth-redirect"),
    path("yellowantauthurl/", request_yellowant_oauth_code, name="yellowant-auth-url"),
    path("yellowant-api/", yellowant_api, name="yellowant-api"),
    url('webhook_receiver/(?P<hash_str>[^/]+)/$', responsewebhook, name='webhook')
]
