import requests
from os import environ as env
from twilio.rest import Client

MY_LAT = 35.0142412
MY_LNG = -85.2519003


def is_rainy():
    params = {'lat': MY_LAT, 'lon': MY_LNG, 'exclude': 'current,minutely,daily', 'appid': openweathermap_key}
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=params).json()['hourly'][:12]
    weather_codes = [[whl_item['id'] for whl_item in weather_data[i]['weather']][0] for i in range(len(weather_data))]
    return all(code < 700 for code in weather_codes)


if is_rainy():
    account_sid = env.get('TWILLO_ACC_SID')
    auth_token = env.get('TWILLO_AUTH_TOK')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid=env.get('TWILLO_MS_SID'),
        body='It is going to rain today',
        to=env.get('SMS_PHONE')
    )

    print(message.sid)
