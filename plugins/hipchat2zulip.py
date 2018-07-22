import os
from errbot import BotPlugin

import zulip


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Download ~/zuliprc-dev from your dev server
client = zulip.Client(config_file=os.path.join(BASE_DIR, "zuliprc"))

# Send a stream message

class Hipchat2zulip(BotPlugin):
    """
    Hipchat to zulip bridge
    """
    def callback_message(self, message):
        request = {
            "type": "stream",
            "to": "Hipchat",
            "subject": message.to.name,
            "content": f'{message.frm.nick}: {message.body}'
        }
        client.send_message(request)