import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from env import *

sender_email = GMAIL_EMAIL
receiver_email = GMAIL_EMAIL
subject = "!!!Inara Trade Routes Alert!!!"
app_password = GMAIL_APP_PASS

def send_email(sender_email, receiver_email, subject, message, app_password, smtp_server="smtp.gmail.com", smtp_port=587):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the MIME object
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Login using the app password
        server.starttls()
        server.login(sender_email, app_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

def get_highest_trade_deal(thread_url):
    response = requests.get(thread_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_traderoutebox = soup.find(class_='traderoutebox')
        div_elements = first_traderoutebox.findChildren("div", recursive=False)

        # Check if there is a second div
        if len(div_elements) >= 2:
            first_station = div_elements[0].get_text(strip=True)[4:].replace("|", " | ")[:-2]
            second_station = div_elements[1].get_text(strip=True)[2:].replace("|", " | ")[:-2]
            first_station_commodity = div_elements[4].find_all("div")[2].get_text(strip=True)
            first_station_supply = div_elements[4].find_all("div")[8].get_text(strip=True)[:-2]
            second_station_commodity = div_elements[8].find_all("div")[2].get_text(strip=True)
            second_station_supply = div_elements[8].find_all("div")[8].get_text(strip=True)[:-2]
            distance = div_elements[9].find_all("div", recursive=False)[0].find_all("div", recursive=False)[0].find_all("div", recursive=False)[1].get_text(strip=True)
            profit = div_elements[9].find_all("div", recursive=False)[1].find_all("div", recursive=False)[1].find_all("div", recursive=False)[1].get_text(strip=True)
            modified_profit = int(''.join(char for char in profit if not char.isalpha()).replace(',', ''))
            # My default setting to be alerted is 20 million per trip or more. This could be lowered or raised based on your needs
            if modified_profit >= 20000000:
                message = "\r\n".join(["From: " + first_station,
                                       "Buy: " + first_station_commodity,
                                       "Supply: " + first_station_supply,
                                       "Deliver To: " + second_station,
                                       "Buy: " + second_station_commodity,
                                       "Supply: " + second_station_supply,
                                       '----------------------------------',
                                       "Route Distance: " + distance,
                                       "Profit Per Trip: " + profit])
                print(message)
                send_email(sender_email, receiver_email, subject, message, app_password)
            else:
                print("No trades high enough to rush for")
        else:
            print("No second div found within the 'traderoutebox' element.")
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")

if __name__ == "__main__":
    # The search criteria can be changed by going to the trade routes page on Inara, entering all the data for your ship/needs,
    # click search, and then copy and paste the url into the url variable below
    url = "https://inara.cz/elite/market-traderoutes/?ps1=Shinrarta+Dezhra&pi10=656&pi2=30&pi5=8&pi3=3&pi9=1000&pi4=0&pi7=2500&pi12=0&pi1=0&pi8=1"
    get_highest_trade_deal(url)