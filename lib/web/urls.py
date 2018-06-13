from django.urls import path
from .views import index, userdetails, delete_integration
from django.conf.urls import url

urlpatterns = [

    path("user/", userdetails, name="home"),
    path('user/<int:integrationId>/delete/', delete_integration, name='home'),
    url(r"^(?P<path>.*)$", index, name="home"),

]
