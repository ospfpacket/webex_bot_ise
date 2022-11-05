import os
from webex_bot.webex_bot import WebexBot
from addmac import AddMAC
from guest_bypass_config import WEBEX_BOT_ACCESS_TOKEN

webex_token = WEBEX_BOT_ACCESS_TOKEN

bot = WebexBot(webex_token, approved_domains=["<approved domain here"], approved_users=["approved users here"]) #Users are case sensitive

bot.add_command(AddMAC())

bot.run()
