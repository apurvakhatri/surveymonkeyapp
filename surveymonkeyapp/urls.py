"""surveymonkeyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from lib.records import urls as records_urls
from lib.web import urls as web_urls
from lib.records.views import integrate_app_account, request_yellowant_oauth_code, yellowant_redirecturl, sm_redirecturl, yellowant_api


urlpatterns = [

    path('admin/', admin.site.urls),
    path("redirecturl/", yellowant_redirecturl),
    path("sm_redirecturl/", sm_redirecturl, name="surveymonkey-auth-redirect"),
    path("yellowantauthurl/", request_yellowant_oauth_code),
    path("yellowant-api/", yellowant_api, name="yellowant-api"),
    path("integrate_app", integrate_app_account),
    path("webhook_receiver/", include(records_urls)),
    path('', include(web_urls))
]
