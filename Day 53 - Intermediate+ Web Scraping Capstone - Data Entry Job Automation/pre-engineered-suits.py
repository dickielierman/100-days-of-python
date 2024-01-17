import requests
from bs4 import BeautifulSoup
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from env import *

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

def search_keywords(text, keywords):
    matching_keywords = [keyword for keyword in keywords if keyword.lower() in text.lower()]
    return matching_keywords

def remove_extra_line_breaks(text):
    # Use regular expression to replace consecutive line breaks with a single line break
    cleaned_text = re.sub(r'\n\s*\n', '\n\n', text)
    return cleaned_text

def get_last_page_url(thread_url):
    response = requests.get(thread_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element containing the total number of pages
        pages_element = soup.find('ul', class_='pageNav-main')
        if pages_element:
            last_page_num = pages_element.find_all("li")[-1].get_text()
            if last_page_num:
                last_page_url = thread_url + '/page-' + last_page_num
                return last_page_url
            else:
                print("Error: Unable to find a link to the last page.")
        else:
            print("Error: Unable to find the element containing page navigation.")
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")



def scrape_for_new_entries(url, keywords):
    sender_email = GMAIL_EMAIL
    receiver_email = GMAIL_EMAIL
    subject = "The Great Pre-Upgraded Gear Sharing is Caring Thread"
    message = "Hello, this is a test email sent from Python using an app password!"

    # App password generated from your Google Account
    app_password = GMAIL_APP_PASS

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        matching_articles = soup.find_all('article', class_='message-body')
        message = ''
        for article in matching_articles:
            if search_keywords(article.get_text(),keywords):
                print(remove_extra_line_breaks(article.get_text()))
                print('##########################################################################################################')
                message = message + remove_extra_line_breaks(article.get_text()) + '\r\n' + '##########################################################################################################'

        if message != '':
            send_email(sender_email, receiver_email, subject, message, app_password)
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")


if __name__ == "__main__":
    thread_url = "https://forums.frontier.co.uk/threads/the-great-pre-upgraded-gear-sharing-is-caring-thread.576352"

    last_page_url = get_last_page_url(thread_url)

    if last_page_url:
        scrape_for_new_entries(last_page_url, ['backpack', 'audio mask'])
    else:
        print("Unable to retrieve the last page URL.")