import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class YellowUserToken(models.Model):
    """User YellowAnt Integration model
    Holds the information which identifies your user with an integration on YA.

    Since a single YA user is allowed to have multiple integrations with your application on YA,
    you need to store a one-to-many relationship for a user to many YA user integrations.

    For example, if this is a mail application, users might want to connect their personal mail
    and work mail with YA. In this case, a single user will have two YA integrations, one which
    connects the personal mail, and the other which connects the work mail.
    Fields:
        user (User): Your application user
        yellowant_integration_token (str): Unique token per integration. This token allows your
            application to perform actions on the YA platform for the YA user integration.
        yellowant_id (int): YA user id
        yellowant_integration_invoke_name (str): YA integration invoke name # each integration of
            your application is controlled by the user with the help of your application's default
            invoke name. Since a YA user is allowed to have multiple integrations with your
            application, YA will suffix the default invoke name for users who want to integrate more
            than once with your application, so that they can control the different integrations
            with their respective invoke names.
        yellowant_integration_id (int): Unique YA user integration id
        webhook_id(str): Unique wehbhook id
        webhook_last_updated(time): The time at which webhook got updated
    """

    user = models.CharField(max_length=100)
    yellowant_token = models.CharField(max_length=100)
    yellowant_id = models.IntegerField(default=0)
    yellowant_integration_invoke_name = models.CharField(max_length=100)
    yellowant_integration_id = models.IntegerField(default=0)
    webhook_id = models.CharField(max_length=100, default="")
    webhook_last_updated = models.DateTimeField(default=datetime.datetime.utcnow)

class YellowAntRedirectState(models.Model):
    """Model to store YA oauth requests with users

    Create a new entry between the user and the oauth state
    Fields:
        user (User): Your application user
        state (str): A unique ID which helps in matching an oauth2 code from YA to a user
    """

    user = models.CharField(max_length=100)
    state = models.CharField(max_length=512, null=False)
    subdomain = models.CharField(max_length=128)

class AppRedirectState(models.Model):
    """Model to store SM oauth requests with users

    Create a new entry between the user and the oauth state
    Fields:
        user (User): Your application user
        state (str): A unique ID which helps in matching an oauth2 code from SM to a user
    """
    user_integration = models.ForeignKey(YellowUserToken, on_delete=models.CASCADE)
    state = models.CharField(max_length=512, null=False)

class SurveyMonkeyUserToken(models.Model):
    """ Model to store the access token received from SurveyMonkey against the YA user.
    Fields:
        user_integration: Your YA application user
        surveymonkey_access_token: SurveyMonkey access token
    """
    user_integration = models.ForeignKey(YellowUserToken, on_delete=models.CASCADE)
    surveymonkey_access_token = models.CharField(max_length=130)

    class Meta:
        unique_together = ('user_integration', 'surveymonkey_access_token')
