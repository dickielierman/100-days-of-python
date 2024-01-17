import smtplib
from env import *


class Message:
    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message

    def send_mail(self):
        with smtplib.SMTP(YAHOO_SMTP, port=587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=YAHOO_EMAIL, password=YAHOO_PASSWORD)
            connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs='richard.lierman@gmail.com', msg=f"Subject:A message from your blog.\n\n"
                                                                                                 f"From: {self.name}\n"
                                                                                                 f"Phone: {self.phone}\n"
                                                                                                 f"Email: {self.email}\n"
                                                                                                 f"Message: {self.message}")
