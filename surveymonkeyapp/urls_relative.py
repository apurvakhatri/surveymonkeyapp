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
from lib.records.views import integrate_app_account


urlpatterns = [
    path('', include(web_urls)),
    path('admin/', admin.site.urls),
    path("surveymonkeyauthurl/", include(records_urls)),
    path("redirecturl/", include(records_urls)),
    path("yellowantauthurl/", include(records_urls)),
    path("webhook_receiver/", include(records_urls)),
    path("integrate_app/", integrate_app_account)
]
