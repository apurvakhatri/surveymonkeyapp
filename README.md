# surveymonkeyapp
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
YellowAnt SurveyMonkey Integration

Go to YellowAnt developers page and click on Generate Developer Token to get "YA_DEVELOPER_TOKEN"

![Screenshot](ya_developer.png)

"HEROKU_APP_NAME" should be same as "App name"

![Screenshot](appname.png)

"OM_CLIENT_ID", "OM_CLIENT_SECRET" is to be obtained from microsoft developers account

Change "Redirect URLs" on microsoft developers account to "https://<appname>.herokuapp.com/outlookredirecttoken/"

## DO NOT ALTER - "DISABLE_COLLECTSTATIC" and "ENV"

After deployment click on "View" and change the URL to /admin/. Example: https://<app-name>.herokuapp.com/admin/


Username: admin

Password: pass

### We request the user to change the ID AND PASSWORD

