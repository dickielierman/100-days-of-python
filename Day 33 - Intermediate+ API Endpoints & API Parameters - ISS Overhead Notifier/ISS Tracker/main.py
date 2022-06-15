import smtplib
from os import environ as env
import requests
from datetime import datetime as dt
from dateutil import parser
import time
MY_LAT = 35.0142412
MY_LNG = -85.2519003
TODAY = dt.utcnow()
print(TODAY)


def in_range(lat, lng):
    if (MY_LAT-5 <= lat <= MY_LAT+5) and (MY_LNG-5 <= lng <= MY_LNG+5):
        return True
    else:
        return False


def is_night():
    params = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    sun_data = requests.get('http://api.sunrise-sunset.org/json', params=params).json()['results']
    sunrise = parser.parse(sun_data['sunrise']).hour
    sunset = parser.parse(sun_data['sunset']).hour
    if TODAY.hour >= sunset or TODAY.hour <= sunrise:
        return False
    else:
        return True


while True:
    time.sleep(60)
    iss_data = requests.get('http://api.open-notify.org/iss-now.json').json()
    latitude = float(iss_data['iss_position']['latitude'])
    longitude = float(iss_data['iss_position']['longitude'])
    if in_range(latitude, longitude) and is_night():
        with smtplib.SMTP(env.get("YAHOO_SMTP"), port=587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=env.get("YAHOO_EMAIL"), password=env.get("YAHOO_PASSWORD"))
            connection.sendmail(from_addr=env.get("YAHOO_EMAIL"), to_addrs='richard.lierman@liermanintl.com', msg=f"Subject:Look up!\n\nThe ISS is above you in the sky!!!")