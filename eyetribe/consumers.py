# In consumers.py
from channels import Group
from channels.sessions import channel_session

# Connected to websocket.connect
@channel_session
def ws_connect(message):
    # Work out room name from path (ignore slashes)

    message.reply_channel.send({
        "text": message.content['text'],
    })