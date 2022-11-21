#Import modules
import os
from webex_bot.webex_bot import WebexBot

#Import the class commands from seperate python files
from bypass import Bypass
from greeting import Greeting
from create import Create
from delete import Delete

#Import the webex bot access token that was generated when you built your bot
#over at developer.webex.com
from webex_access_token import WEBEX_BOT_ACCESS_TOKEN

#Set parameters for the bot.
bot = WebexBot(WEBEX_BOT_ACCESS_TOKEN, approved_users=["User1", "User2"])

#Call in the commands for use with the bot
bot.add_command(Bypass())
bot.add_command(Greeting())
bot.add_command(Create())
bot.add_command(Delete())

#Run the bot
bot.run()
