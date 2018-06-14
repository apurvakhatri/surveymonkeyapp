from .views import  responsewebhook
from django.conf.urls import url

urlpatterns = [
    url('webhook_receiver/(?P<hash_str>[^/]+)/$', responsewebhook, name='webhook')
]
