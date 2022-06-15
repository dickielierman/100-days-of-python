from twilio.rest import Client
from os import environ as env
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = env.get('TWILLO_ACC_SID')
        self.token = env.get('TWILLO_AUTH_TOK')

    def send_note(self, message_text):
        client = Client(self.sid, self.token)
        self.message = client.messages.create(
            messaging_service_sid=env.get('TWILLO_MS_SID'),
            body=message_text,
            to=env.get('SMS_PHONE')
        )

        print(self.message.sid)