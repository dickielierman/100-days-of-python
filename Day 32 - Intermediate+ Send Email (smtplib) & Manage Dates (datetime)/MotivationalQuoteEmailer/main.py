import smtplib
from os import environ as env
from random import choice

from datetime import datetime as dt

if dt.now().weekday() == 2:
    with open('quotes.txt') as quote_file:
        quote_of_the_day = choice(quote_file.readlines())


    with smtplib.SMTP(env.get("YAHOO_SMTP"), port=587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=env.get("YAHOO_EMAIL"), password=env.get("YAHOO_PASSWORD"))
        connection.sendmail(from_addr=env.get("YAHOO_EMAIL"), to_addrs='richard.lierman@liermanintl.com', msg=f"Subject:Quote of the day\n\n{quote_of_the_day}")
