from django.urls import path

from .views import index, userdetails, delete_integration
from django.conf.urls import url

urlpatterns = [
    path("", index, name="home"),
    path("user/", userdetails, name="home"),
    path('user/<int:integrationId>/delete/', delete_integration, name='home')


    #path("(?P<user_integration_id>)/delete/", delete_integration, name="home")
    #path("(?P<article_id>\d+)/delete/",delete_integration, name="home")

]
