from webex_bot.models.command import Command
import requests
import json

class Create(Command):
    def __init__(self):
        super().__init__(
            command_keyword="create",
            help_message="Add an endpoint to ISE",
            card=None,
        )
    
    def execute(self, message, attachment_action, activity):
        
        message = message.split(' ')     #This section allows you to interact with the bot in a direct message or in a teams space
        if len(message) == 3:
          message = message[2]
        else:
          message = message[1]
        
        mac_addr = message

        url = "https://<ise_server:port>/ers/config/endpoint"     #Put ISE Server name in URL with port

        payload = json.dumps({
            "ERSEndPoint": {
            "name": mac_addr,
            "mac": mac_addr
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': '<Basic64 Auth>'     #Put the basic64 auth here for your username and password
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify = False)

        return("Endpoint " + mac_addr + " has been added to ISE.")