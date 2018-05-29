"""This file contains the logic to understand a user message request from YA and return
a response in the format of a YA message object accordingly
"""
import json
import traceback
import datetime
import requests
import pytz
from yellowant import YellowAnt
from django.conf import settings
from yellowant.messageformat import MessageClass, MessageAttachmentsClass,\
MessageButtonsClass, AttachmentFieldsClass
from .models import SurveyMonkeyUserToken, YellowUserToken



class CommandCenter(object):
    """Handles user commands

    Args:
        yellowant_user_id (int): The user id of the YA user
        yellowant_integration_id (int): The integration id of a YA user
        command_name (str): Invoke name of the command the user is calling
        args (dict): Any arguments required for the command to run
    """
    def __init__(self, yellowant_user_id, yellowant_intergration_id, function_name, args):
        self.yellowant_user_id = yellowant_user_id
        self.yellowant_intergration_id = yellowant_intergration_id
        self.function_name = function_name
        self.args = args

    def parse(self):
        self.commands = {
            'AccountDetails': self.Account_Details,
            'ViewAllContacts': self.View_All_Contacts,
            'workgroup': self.workgroup_details,
            'ContactLists': self.Contact_Lists,
            'ContactListDetails': self.Contact_List_Details,
            'ViewSurveys': self.View_Surveys,
            'ViewSurveyDetails': self.View_Survey_Details,
            'view_survey_expanded_details': self.view_survey_expanded_details,
            'SurveyCategory': self.Survey_Category,
            'SurveyTemplates': self.Survey_Templates,
            'SurveyLangAvailable': self.Survey_Lang_Available,
            'CollectorsAvailable': self.Collectors_Available,
            'Webhooks': self.Webhooks,
            'ViewWebhook': self.ViewWebhook
        }
        print("In parse")

        self.user_integration = YellowUserToken.objects.get(\
        yellowant_intergration_id=self.yellowant_intergration_id)

        self.sm_access_token_object = SurveyMonkeyUserToken.objects.get(\
        user_integration=self.user_integration)

        self.surveymonkey_access_token = self.sm_access_token_object.surveymonkey_access_token
        self.headers = {\
            "Authorization" :"bearer %s" %(self.surveymonkey_access_token),\
            "Content-Type": "application/json"\
        }
        if self.user_integration.webhook_last_updated + datetime.timedelta(days=1) < pytz.utc.localize(datetime.datetime.utcnow()):
            self.RefreshWebhooks()

        # build YA message object
        return self.commands[self.function_name](self.args)

    def Account_Details(self, args):
        """ It is used to return the account details of the user.
        Details like username, first name, email, account type, last login, id, etc.
        """
        print("In account details")

        data = {}

        url = (settings.SM_API_BASE + settings.USER_INFO_ENDPOINT)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        print(response_json)
        message = MessageClass()
        attachment = MessageAttachmentsClass()
        field1 = AttachmentFieldsClass()
        field1.title = "Username"
        field1.value = response_json["username"]
        attachment.attach_field(field1)

        field2 = AttachmentFieldsClass()
        field2.title = "First name"
        field2.value = response_json["first_name"]
        attachment.attach_field(field2)

        field6 = AttachmentFieldsClass()
        field6.title = "Email"
        field6.value = response_json["email"]
        attachment.attach_field(field6)

        field3 = AttachmentFieldsClass()
        field3.title = "Last name"
        field3.value = response_json["last_name"]
        attachment.attach_field(field3)


        field4 = AttachmentFieldsClass()
        field4.title = "Account type"
        field4.value = response_json["account_type"]
        attachment.attach_field(field4)

        field5 = AttachmentFieldsClass()
        field5.title = "Email ver"
        field5.value = response_json["email_verified"]
        attachment.attach_field(field5)



        field7 = AttachmentFieldsClass()
        field7.title = "Last login"
        field7.value = response_json["date_last_login"]
        attachment.attach_field(field7)

        field8 = AttachmentFieldsClass()
        field8.title = "ID"
        field8.value = response_json["id"]
        attachment.attach_field(field8)




        message.message_text = "Here are the account details:"
        message.attach(attachment)

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def View_All_Contacts(self, args):
        #Display all the Contacts of the user. Including their details.
        print("In ViewAllContacts")
        url = "https://api.surveymonkey.com/v3/contacts/bulk"
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        print(response_json)
        data = response_json["data"]
        message = MessageClass()
        message.message_text = "All Contacts: \n"
        for i in range(len(data)):
            attachment = MessageAttachmentsClass()
            obj = data[i]

            field1 = AttachmentFieldsClass()
            field1.title = "First Name"
            field1.value = obj["first_name"]
            attachment.attach_field(field1)

            field2 = AttachmentFieldsClass()
            field2.title = "Last Name"
            field2.value = obj["last_name"]
            attachment.attach_field(field2)

            field3 = AttachmentFieldsClass()
            field3.title = "Email"
            field3.value = obj["email"]
            attachment.attach_field(field3)

            field4 = AttachmentFieldsClass()
            field4.title = "Status"
            field4.value = obj["status"]
            attachment.attach_field(field4)

            message.attach(attachment)

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def workgroup_details(self, args):
        print("In workgroupdetails")
        user_id = int(args['User-id'])
        print(user_id)
        s = requests.Session()
        headers = s.headers.update({
            "Authorization": "Bearer %s" % self.surveymonkey_access_token,
            "Content-Type": "application/json"
            })

        url = "https://api.surveymonkey.com/v3/users/%s/workgroups" % user_id
        response = s.get(url)

        print(response)
        print(response.content)
        return "workgroup got"


    def Contact_List_Details(self, args):
        # List all the details of the contact lists(groups) the user has created.
        print("ContactListDetails")
        contact_list_id = args["ContactListId"]
        url = "https://api.surveymonkey.com/v3/contact_lists/%s/contacts"%(contact_list_id)

        try:
            message = MessageClass()
            message.message_text = "Contacts details: \n"
            response = requests.get(url, headers=self.headers)
            response_json = response.json()
            print(response_json)
            data = response_json["data"]
            for i in range(len(data)):
                obj = data[i]
                attachment = MessageAttachmentsClass()

                field1 = AttachmentFieldsClass()
                field1.title = "First name"
                field1.value = obj["first_name"]
                attachment.attach_field(field1)

                field2 = AttachmentFieldsClass()
                field2.title = "Last name"
                field2.value = obj["last_name"]
                attachment.attach_field(field2)

                field4 = AttachmentFieldsClass()
                field4.title = "Email"
                field4.value = obj["email"]
                attachment.attach_field(field4)

                field3 = AttachmentFieldsClass()
                field3.title = "Id"
                field3.value = obj["id"]
                attachment.attach_field(field3)


                message.attach(attachment)

            # use inbuilt sdk method to_json to return message in a json format accepted by YA
            return message.to_json()
        except Exception as e:
            print("Exception occured is")
            print(str(e))
            traceback.print_exc()

    def Contact_Lists(self, args):
        # List all the contact lists(groups) the user has created.
        user_id = self.user_integration.yellowant_intergration_id
        print("In viewlists")

        url = (settings.SM_API_BASE + settings.VIEW_CONTACTLISTS)
        try:
            message = MessageClass()
            message.message_text = "Contact list:\n"
            attachment = MessageAttachmentsClass()

            response = requests.get(url, headers=self.headers)
            response_json = response.json()
            print(response_json)
            data = response_json["data"]
            print(data[0]['id'])
            send_data = {\
            'list':[]\
            }
            for i in range(len(data)):
                button1 = MessageButtonsClass()
                print(i)
                obj = data[i]
                name = obj["name"]
                print(name)
                id = obj["id"]
                print(id)
                send_data['list'].append({'id':id, 'name':name})
                button1.text = name
                button1.value = name
                button1.name = name
                button1.command = {
                    "service_application": user_id,
                    "function_name": "ContactListDetails",\
                     "data":{\
                     "ContactListId":id\
                     }
                }
                attachment.attach_button(button1)
            message.attach(attachment)
            message.data = send_data

            # use inbuilt sdk method to_json to return message in a json format accepted by YA
            return message.to_json()
        except Exception as e:
            print("Exception occured is")
            print(str(e))
            traceback.print_exc()

    def View_Surveys(self, args):
        # Display the Surveys associated with the users account.
        print("In view surveys")
        user_id = self.user_integration.yellowant_intergration_id
        url = (settings.SM_API_BASE + settings.VIEW_SURVEY)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        print(response_json)
        data = response_json["data"]
        send_data = {
            "surveys": []
        }
        message = MessageClass()
        message.message_text = "Surveys"
        for i in range(len(data)):
            attachment = MessageAttachmentsClass()
            send_data['surveys'].append({'id':data[i]["id"], 'title':data[i]["title"]})
            obj = data[i]
            title = obj["title"]
            id = obj["id"]
            button1 = MessageButtonsClass()
            attachment.title = title

            field1 = AttachmentFieldsClass()
            field1.title = "ID"
            field1.value = id
            attachment.attach_field(field1)

            button1.text = "Know more"
            button1.value = id
            button1.name = id
            button1.command = {
                "service_application": user_id,
                "function_name": "ViewSurveyDetails",
                "data":{\
                "SurveyId":id\
                }
            }
            attachment.attach_button(button1)
            message.attach(attachment)
        message.data = send_data
        print(message)

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def View_Survey_Details(self, args):
        # Gives the details of the survey(whichever the user chooses).
        print("In view_details")
        survey_id = args["SurveyId"]

        url = ("https://api.surveymonkey.com/v3/surveys/%s")%(survey_id)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        print(response_json)
        title = response_json["title"]
        message = MessageClass()
        attachment = MessageAttachmentsClass()
        message.message_text = title

        field1 = AttachmentFieldsClass()
        field1.title = "Response Count"
        field1.value = response_json["response_count"]
        attachment.attach_field(field1)

        field2 = AttachmentFieldsClass()
        field2.title = "Date Created"
        field2.value = response_json["date_created"]
        attachment.attach_field(field2)

        field3 = AttachmentFieldsClass()
        field3.title = "Question Count"
        field3.value = response_json["question_count"]
        attachment.attach_field(field3)

        field4 = AttachmentFieldsClass()
        field4.title = "Category"
        field4.value = response_json["category"]
        attachment.attach_field(field4)

        field5 = AttachmentFieldsClass()
        field5.title = "Category"
        field5.value = response_json["category"]
        attachment.attach_field(field5)

        field7 = AttachmentFieldsClass()
        field7.title = "Ownership"
        field7.value = response_json["is_owner"]
        attachment.attach_field(field7)

        field8 = AttachmentFieldsClass()
        field8.title = "Date modified"
        field8.value = response_json["date_modified"]
        attachment.attach_field(field8)

        field6 = AttachmentFieldsClass()
        field6.title = "Survey Preview"
        field6.value = "<{}|Preview>".format(response_json["preview"])
        attachment.attach_field(field6)

        field9 = AttachmentFieldsClass()
        field9.title = "Analyze Survey"
        field9.value = "<{}|Analyze>".format(response_json["analyze_url"])
        attachment.attach_field(field9)

        field10 = AttachmentFieldsClass()
        field10.title = "Survey summary"
        field10.value = "<{}|Summary>".format(response_json["summary_url"])
        attachment.attach_field(field10)

        field11 = AttachmentFieldsClass()
        field11.title = "Edit survey"
        field11.value = "<{}|Edit>".format(response_json["edit_url"])
        attachment.attach_field(field11)

        field12 = AttachmentFieldsClass()
        field12.title = "View Response"
        field12.value = "<{}|Edit>".format(response_json["collect_url"])
        attachment.attach_field(field12)

        message.attach(attachment)

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def view_survey_expanded_details(self, args):
        # Display the Questions and other details associated with a
        # particular survey which user chooses.
        print("In view_expanded_details")
        survey_id = args["Survey-id"]

        url = ("https://api.surveymonkey.com/v3/surveys/%s/details")%(survey_id)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        pages = response_json["pages"]
        message = MessageClass()
        result = "Questions are: \n"
        for i in range(len(pages)):
            questions = pages[i]["questions"]
            for j in range(len(questions)):
                headings = questions[j]["headings"]
                heading = headings[0]
                question = heading["heading"]
                result = result + str(j+1)+ ":" + " " + question + "\n"
        message.message_text = result

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def Survey_Category(self, args):
        print("In SurveyCategory")
        url = (settings.SM_API_BASE + settings.SURVEY_CATEGORY)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        result = "Survey Categories are: \n"
        message = MessageClass()
        data = response_json["data"]
        for i in range(len(data)):
            obj = data[i]
            id = obj["id"]
            name = obj["name"]
            result = result+str(i+1)+ "." + "Id is: "+ id + "  " + "Name of category: "+ name +"\n"
        message.message_text = result

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def Survey_Templates(self, args):
        # Return a list of templates available to create a new surey
        print("In SurveyTemplates")

        url = (settings.SM_API_BASE + settings.SURVEY_TEMPLATES)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        data = response_json["data"]
        message = MessageClass()
        result = "Templates are: \n"
        for i in range(len(data)):
            obj = data[i]
            name = obj["name"]
            print(name)
            result = result + str(i+1)+":" + name + "\n"
        message.message_text = result

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def Survey_Lang_Available(self, args):
        # Return the available languages in which the Survey can be translated.
        print("In SurveyLangAvailable")
        survey_id = args["Survey-ID"]

        url = "https://api.surveymonkey.com/v3/surveys/%s/languages"%(survey_id)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        print(response_json)
        data = response_json["data"]
        message = MessageClass()
        result = "Languages available are: \n"
        for i in range(len(data)):
            obj = data[i]
            lang = obj["name"]
            id = obj["id"]
            result = result + lang + " " + "ID is: "+ id+ "\n"
        message.message_text = result

        # use inbuilt sdk method to_json to return message in a json format accepted by YA
        return message.to_json()

    def Collectors_Available(self, args):
        print("In view_details")
        survey_id = args["SurveyId"]

        url = "https://api.surveymonkey.com/v3/surveys/%s/collectors"%(survey_id)
        message = MessageClass()
        result = "Collectors available are: \n"
        try:
            response = requests.get(url, headers=self.headers)
            response_json = response.json()
            data = response_json["data"]
            send_data = {\
            "collectors":[]\
            }
            for i in range(len(data)):
                obj = data[i]
                name = obj["name"]
                id = obj["id"]
                send_data["collectors"].append({"id":id, "name":name})
                result = result + str(i+1)+": "+ name+" "+ "ID is: "+ id+"\n"
            message.data = send_data
            message.message_text = result
            print(send_data)

            # use inbuilt sdk method to_json to return message in a json format accepted by YA
            return message.to_json()
        except Exception as e:
            print(str(e))
            traceback.print_exc()

    # def Collectors(self, args):
    #     print("In collectors")
    #     CollectorId = args["CollectorId"]
    #
    #     url = "https://api.surveymonkey.com/v3/collectors/%s"%(CollectorId)
    #     response = requests.get(url, headers=self.headers)
    #     response_json = response.json()
    #
    #     print(response_json)
    #     return "Hey"

    def Webhooks(self, args):
        print("In Webhooks")
        app_name = settings.app_name
        data = {
        "name": "My Webhook",
	    "event_type": "response_completed",
	    "object_type": "survey",
	    "object_ids":["151123389"],
	    "subscription_url": "https://{}.herokuapp.com/webhook_receiver/webhook_receiver/".format(app_name)
        }

        url = "https://api.surveymonkey.com/v3/webhooks"
        response = requests.post(url, headers=self.headers, json=(data))
        response_json = response.json()
        print(response_json)
        return "Hey"

    def RefreshWebhooks(self):
        print("In RefreshWebhooks")
        self.user_integration.webhook_last_updated = datetime.datetime.utcnow()
        self.user_integration.save()

        user_integration = YellowUserToken.objects.get(\
        yellowant_intergration_id=self.yellowant_intergration_id)

        sm_access_token_object = SurveyMonkeyUserToken.objects.get(\
        user_integration=user_integration)

        surveymonkey_access_token = sm_access_token_object.surveymonkey_access_token
        headers = {\
            "Authorization" :"Bearer %s" %(surveymonkey_access_token),\
            "Content-Type": "application/json"\
        }

        url = (settings.SM_API_BASE + settings.VIEW_SURVEY)
        response = requests.get(url, headers=headers)
        response_json = response.json()
        surveys_data = response_json["data"]

        url = (settings.SM_API_BASE + settings.VIEW_WEBHOOKS)
        response = requests.get(url, headers=headers)
        response_json = response.json()
        webhooks_data = response_json["data"]

        surveys_webhooks_enabled = []

        for wh in webhooks_data['data']:
            surveys_webhooks_enabled += wh['object_ids']

        surveys_to_enable = []
        for survey in surveys_data:
            if survey['id'] not in surveys_webhooks_enabled:
                surveys_to_enable.append(survey['id'])

        app_name = settings.app_name
        data = {
        "name": "My Webhook",
	    "event_type": "response_completed",
	    "object_type": "survey",
	    "object_ids": surveys_to_enable,
	    "subscription_url": "http://%s.herokuapp.com/webhook_receiver/webhook_receiver/%s/"%(app_name,self.user_integration.webhook_id)
        }

        url = "https://api.surveymonkey.com/v3/webhooks"
        response = requests.post(url, headers=headers, json=(data))
        response_json = response.json()


    def ViewWebhook(self, args):
        print("In ViewWebhook")
        WebhookId = args["WebhookId"]
        url = "https://api.surveymonkey.com/v3/webhooks/%s"%(WebhookId)
        response = requests.get(url, headers=self.headers)
        response_json = response.json()
        print(response_json)
        return "HEY"
