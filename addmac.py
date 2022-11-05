from webex_bot.models.command import Command
import requests
import json

class AddMAC(Command):
    def __init__(self):
        super().__init__(
            command_keyword="addmac",
            help_message="Add MAC to Guset Bypass",
            card=None,
        )
    
    def execute(self, message, attachment_action, activity):

        url = "https://<ise url here>:9060/ers/config/endpoint/name/"+ message

        payload={}
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': '<Basic 64 Auth Here>' #https://www.debugbear.com/basic-auth-header-generator
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify = False)
        response = json.loads(response.text)
        response = response.get('ERSEndPoint')
        ep_id = (response['id'])

        url = "https://<ise url here>:9060/ers/config/endpoint/"+ ep_id

        payload = json.dumps({
          "ERSEndPoint": {
          "groupId": "<ise group id here>",
          "staticGroupAssignment": True
        }
        })
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': '<Basic 64 Auth Here>' #https://www.debugbear.com/basic-auth-header-generator
        }

        response = requests.request("PUT", url, headers=headers, data=payload, verify = False)

        return (response.text)
