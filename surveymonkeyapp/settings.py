"""
Django settings for surveymonkeyapp project.


Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import json

# get app credentials from json
data = open('yellowant_app_credentials.json').read()
data_json = json.loads(data)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','($g%68la(r_u!0i9h^=cv^e(3$2tj^tp_#%s$mwu7@3vhxzq%o')
#'($g%68la(r_u!0i9h^=cv^e(3$2tj^tp_#%s$mwu7@3vhxzq%o'

# SECURITY WARNING: don't run with debug turned on in production!
app_name = os.environ.get("HEROKU_APP_NAME")
BASE_URL = "https://8c3ab50d.ngrok.io/"
DEBUG = True

BASE_HREF = "/"
SITE_PROTOCOL = "https://"

ALLOWED_HOSTS = ['*', '{}.herokuapp.com'.format(app_name)]


DEV_ENV = os.environ.get('ENV', 'DEV')
if DEV_ENV=="DEV":
    SURVEYMONKEY_CLIENT_ID = "lkE_cJOzRV6j0B9bPLaJug"
    SURVEYMONKEY_CLIENT_SECRET = "65085943951230993449921484314018791204"
    SURVEYMONKEY_VERIFICATION_TOKEN = "pd45cmph4w8I7hrPUIUPin5-u9vMuWm1PDChgAoHQkTyHndCqtT3224Rcn1582NIqaJNNdIDsByaJOFXojIbXKwFkp35e5yFdhCSHefGfoFgukpxrNsIjVakiSXvxmLk"
    BASE_URL = "https://8c3ab50d.ngrok.io/"
    SITE_DOMAIN_URL = "ngrok.io"

elif DEV_ENV=="HEROKU":
    BASE_URL = "https://{}.herokuapp.com/".format(app_name)
    SURVEYMONKEY_CLIENT_ID = os.environ.get('SM_CLIENT_ID')
    SURVEYMONKEY_CLIENT_SECRET = os.environ.get('SM_CLIENT_SECRET')
    SURVEYMONKEY_VERIFICATION_TOKEN = os.environ.get('SM_VERIFICATION_TOKEN')
    app_name = os.environ.get("HEROKU_APP_NAME")
    SITE_DOMAIN_URL = "herokuapp.com"


SURVEYMONKEY_OUTH_URL = "https://api.surveymonkey.com/oauth/authorize/"


# URL to receive oauth2 codes from SM for user authentication. As a developer, you need to provide
# this URL in the SM
# developer console so that SM knows exactly where to send the oauth2 codes
SURVEYMONKEY_REDIRECT_URL = BASE_URL + "sm_redirecturl/"

YELLOWANT_OAUTH_URL = "https://www.yellowant.com/api/oauth2/authorize/"


# YellowAnt specific settings
YA_APP_ID = str(data_json['application_id'])
# Client ID generated from the YA developer console. Required to identify requests from
# this application to YA
YELLOWANT_CLIENT_ID = str(data_json['client_id'])
# Client secret generated from the YA developer console. Required to identify requests from
# this application to YA
YELLOWANT_CLIENT_SECRET = str(data_json['client_secret'])
# Verification token generated from the YA developer console. This application can verify requests
# from YA as they will
# carry the verification token
YELLOWANT_VERIFICATION_TOKEN = str(data_json['verification_token'])
# URL to receive oauth2 codes from YA for user authentication. As a developer, you need to provide
# this URL in the YA
# developer console so that YA knows exactly where to send the oauth2 codes.
YELLOWANT_REDIRECT_URL = BASE_URL + "redirecturl/"

# Application definition

SM_API_BASE = "https://api.surveymonkey.com"
USER_INFO_ENDPOINT = "/v3/users/me"
VIEW_CONTACTLISTS = "/v3/contact_lists"
VIEW_SURVEY = "/v3/surveys"
VIEW_WEBHOOKS = "/v3/webhooks"
SURVEY_CATEGORY = "/v3/survey_categories"
SURVEY_TEMPLATES = "/v3/survey_templates"
USER_WORKGROUP_ENDPOINT = "/v3/users/user_id=%s/workgroups"


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lib.records',
    'lib.web'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'surveymonkeyapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'surveymonkeyapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'surveymonkey5',
        'USER': 'root',
        'PASSWORD': 'khatri@19',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# The dj_database_url is used for deployment on heroku.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# STATIC_URL = ('web/static/')
# STATIC_ROOT = os.path.join(BASE_DIR, 'web/static/')
