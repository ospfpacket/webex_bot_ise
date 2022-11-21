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
        response = json.loads(response.text)
        response = response.get('ERSEndPoint')
        ep_id = (response['id'])

        url = "https://<ise_server:port>/ers/config/endpoint/" + ep_id     #Put ISE Server name in URL with port

        payload={}
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': '<Basic64 Auth>'     #Basic Auth 64 is used
        }

        response = requests.request("DELETE", url, headers=headers, data=payload, verify = False)

        return ("MAC Address " + mac_addr + " has been removed from ISE!")
