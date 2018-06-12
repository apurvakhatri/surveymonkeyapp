import os
DEV_ENV=os.environ.get("ENV")
print(DEV_ENV)
if DEV_ENV=="HEROKU":
    YA_DEVELOPER_TOKEN=os.environ.get("YA_DEVELOPER_TOKEN")
    print(YA_DEVELOPER_TOKEN)
    base=os.environ.get("HEROKU_APP_NAME")
    #website = "https://{}.herokuapp.com/".format(base)
    #api_url = "https://{}.herokuapp.com/yellowantauthurl/yellowant-api/".format(base)
    #installation_website = "https://{}.herokuapp.com/".format(base)
    #privacy_policy = "http://yellowant.com/privacy"
    website = "https://{}.herokuapp.com/".format(base)

    os.system("yellowant auth --token {} --host https://www.yellowant.com ".format(YA_DEVELOPER_TOKEN))
    os.system('yellowant sync -q --api_url {}yellowantauthurl/yellowant-api/ --website {} --install_page_url {} --privacy_policy_url {}privacy --redirect_uris {}redirecturl/yellowant_redirecturl/'.format(website,website,website,website,website))
    os.system('ls -al')
    #os.system("yellowant pull 322")
    #os.system('printf "{}\n{}\n{}\n{}\n{}\n{}" |yellowant create '.format(invoke,website,api_url,installation_website,privacy_policy,redirect_url))
