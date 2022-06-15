import smtplib
from os import environ as env
from random import choice
from datetime import datetime as dt
import pandas as pd
from os import listdir

data = pd.read_csv('birthdays.csv')
birthday_dict = data.to_dict(orient='index')
BIRTHDAYS = [v for (k,v) in birthday_dict.items()]
TODAY = dt.now()
LETTER_DIR = 'letter_templates/'
LETTERS = [l for l in listdir(LETTER_DIR)]
SIGNER = 'Dickie'

for person in BIRTHDAYS:
    if person['month'] == TODAY.month and person['day'] == TODAY.day:
        random_letter = choice(LETTERS)
        with open(LETTER_DIR+random_letter) as f:
            birthday_wish = f.read().replace('[NAME]', person['name']).replace('[signed]', SIGNER)
        with smtplib.SMTP(env.get("YAHOO_SMTP"), port=587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=env.get("YAHOO_EMAIL"), password=env.get("YAHOO_PASSWORD"))
            connection.sendmail(from_addr=env.get("YAHOO_EMAIL"), to_addrs='richard.lierman@liermanintl.com', msg=f"Subject:Happy Birthday, {person['name']}!!!\n\n{birthday_wish}")
