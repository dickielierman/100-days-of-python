from twilio.rest import Client
import env
import smtplib
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = env.TWILLO_ACC_SID
        self.token = env.TWILLO_AUTH_TOK

    def send_note(self, message_text):
        client = Client(self.sid, self.token)
        self.message = client.messages.create(
            messaging_service_sid=env.TWILLO_MS_SID,
            body=message_text,
            to=env.SMS_PHONE
        )

        print(self.message.sid)

    def send_email(self, email, message):
        with smtplib.SMTP(env.YAHOO_SMTP, port=587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=env.YAHOO_EMAIL, password=env.YAHOO_PASSWORD)
            connection.sendmail(from_addr=env.YAHOO_EMAIL, to_addrs=email, msg=f"Subject:Low price alert!\n\n{message}")
