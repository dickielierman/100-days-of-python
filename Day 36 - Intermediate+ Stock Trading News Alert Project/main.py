import requests
from os import environ as env
from datetime import date
from twilio.rest import Client

STOCKS = [{"code": "TSLA", "name": "Tesla Inc"}]
AV_API = 'https://www.alphavantage.co/query'
AV_API_KEY = env.get("AV_API_KEY")

NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY = env.get("NEWS_API_KEY")
today = date.today()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def send_text(message_text):
    account_sid = env.get('TWILLO_ACC_SID')
    auth_token = env.get('TWILLO_AUTH_TOK')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid=env.get('TWILLO_MS_SID'),
        body=message_text,
        to=env.get('SMS_PHONE')
    )

    print(message.sid)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news(company_name):
    params = {
        "q": company_name,
        "from": str(today),
        "sortBy": 'popularity',
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    news = requests.get(NEWS_API, params=params)
    news_data = news.json()["articles"]
    sender = [[d['title'], d['description']]for d in news_data[:3]]
    return sender


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
for stock in STOCKS:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock['code'],
        "apikey": env.get('AV_API_KEY')
    }
    r = requests.get(AV_API, params=params)
    data = r.json()['Time Series (Daily)']
    data_list = [val for key, val in data.items()]
    yesterday_close = float(data_list[0]["4. close"])
    day_before_close = float(data_list[1]["4. close"])
    difference = abs(yesterday_close - day_before_close)
    diff_percent = (difference / yesterday_close) * 100
    if diff_percent > 5:
        news = get_news(stock['name'])
        for article in news:
            send_text(f"{stock['code']}: {'🔺' if yesterday_close > day_before_close else '🔻'}{round(diff_percent)}%\nHeadline: {article[0]}\nBrief: {article[1]}")

