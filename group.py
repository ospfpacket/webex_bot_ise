#Import modules to be used in this command
from webex_bot.models.command import Command
import requests
import json

with open("groupInput.json", "r") as card:
    INPUT_CARD = json.load(card)

class Group(Command):
    def __init__(self):
        super().__init__(
            command_keyword="group",
            help_message="Add MAC to Select ISE Groups",
            card=INPUT_CARD,
        )
    
    def execute(self, message, attachment_action, activity):
       
        mac_addr = attachment_action.inputs['mac_addr']
        group_id = attachment_action.inputs['group_id']

        url = "https://<ISE URL:PORT>/ers/config/endpoint/name/"+ mac_addr

        payload={}
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic64 Auth Here'     #Basic Auth 64 is used
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify = False)     #SSL Verification is turned off. Should be enabled in production.

        #print(response.status_code)     #This is for debugging in the console

        if response.status_code == 200:
            #This parses the mac address endpoint id and sets the variable ep_id
            response = json.loads(response.text)
            response = response.get('ERSEndPoint')
            ep_id = (response['id'])
        elif response.status_code == 404:
            return("Endpoint was not found in ISE. Please verify the MAC address and try again.")
        elif response.status_code == 500:
            return("Invalid MAC. Please verify the MAC address and try again.")
        else:
            return("Unhandled Exception. Please contact your system administrator.")

        url = "https://<ISE URL:PORT>/ers/config/endpoint/"+ ep_id

        payload = json.dumps({
            "ERSEndPoint": {
            "groupId": group_id,
            "staticGroupAssignment": True
          }
        })

        response = requests.request("PUT", url, headers=headers, data=payload, verify = False)
        
        #print(response.status_code)     #This is for debugging in the console

        if response.status_code == 200:
            return(mac_addr + " has been added to your selected group.")
        else:
            return("Unhandled Exception. Please contact your system administrator.")
