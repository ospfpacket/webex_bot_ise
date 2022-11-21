from webex_bot.models.command import Command

class Greeting(Command):
    def __init__(self):
        super().__init__(
            command_keyword="hello",
            help_message="Send back a Greeting",
            card=None,
        )
    
    def execute(self, message, attachment_action, activity):
        return "Hello, I am the Guest Bypass Bot!"