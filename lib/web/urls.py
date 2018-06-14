from django.urls import path
from .views import index, userdetails, delete_integration
from django.conf.urls import url

urlpatterns = [
    # path("", index, name="home"),
    path("user/", userdetails, name="home"),
    path('user/<int:integrationId>/delete/', delete_integration, name='home'),
    url(r"^account/(?P<path>.*)$", index, name="home")

]
