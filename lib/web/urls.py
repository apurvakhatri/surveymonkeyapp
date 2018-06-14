from django.urls import path
from .views import index, userdetails, delete_integration
from django.conf.urls import url

urlpatterns = [
    # path("", index, name="home"),
    path("user/", userdetails, name="user_integrations"),
    path('user/<int:integrationId>/delete/', delete_integration, name='user_integration_delete'),
    url(r"^(?P<path>.*)$", index, name="home"),

]
