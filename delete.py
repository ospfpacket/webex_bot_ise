from webex_bot.models.command import Command
import requests
import json

class Delete(Command):
    def __init__(self):
        super().__init__(
            command_keyword="delete",
            help_message="Delete MAC from ISE",
            card=None,
        )
    
    def execute(self, message, attachment_action, activity):

        message = message.split(' ')     #This section allows you to interact with the bot in a direct message or in a teams space
        if len(message) == 3:
            message = message[2]
        else:
            message = message[1]

        mac_addr = message
        
        url = "https://<ise_server:port>/ers/config/endpoint/name/"+ mac_addr     #Put ISE Server name in URL with port

        payload={}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic64 Auth>'     #Basic Auth 64 is used
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify = False)
        
        print(response.status_code)     #This is for debugging in the console
        
        if response.status_code == 200:
            response = json.loads(response.text)
            response = response.get('ERSEndPoint')
            ep_id = (response['id'])
        elif response.status_code == 404:
            return("Endpoint was not found in ISE. Please verify the MAC address and try again.")
        else:
            return("Unhandled Exception. Please contact your system administrator.")

        url = "https://<ise_server:port>/ers/config/endpoint/" + ep_id     #Put ISE Server name in URL with port

        response = requests.request("DELETE", url, headers=headers, data=payload, verify = False)
        if response.status_code == 204:
            return ("MAC Address " + mac_addr + " has been removed from ISE!")
        elif response.status_code == 404:
            return("Endpoint was not found in ISE. Please verify the MAC address and try again.")
        else:
            return("Unhandled Exception. Please contact your system administrator.")
