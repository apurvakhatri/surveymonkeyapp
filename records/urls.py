from django.urls import path
from django.conf.urls import include
from records.views import surveymonkeyRedirecturl, redirectToYellowAntAuthenticationPage , yellowantRedirecturl, yellowant_api, responsewebhook
from django.conf.urls import url

urlpatterns = [
    path("redirecturl/", surveymonkeyRedirecturl, name="surveymonkey-auth-redirect"),
    path("yellowantredirecturl/", yellowantRedirecturl, name="yellowant-auth-redirect"),
    path("yellowantauthurl/", redirectToYellowAntAuthenticationPage, name="yellowant-auth-url"),
    path("yellowant-api/", yellowant_api, name="yellowant-api"),
    url('webhook_receiver/(?P<hash_str>[^/]+)/$', responsewebhook, name='webhook')
]
