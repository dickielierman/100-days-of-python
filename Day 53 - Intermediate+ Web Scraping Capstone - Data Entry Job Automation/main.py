from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from env import *
from time import sleep
from pprint import pprint
from bs4 import BeautifulSoup
import requests as req


def save_listing(a,p,l):
    driver = SELENIUM_BROWSER("chrome", True)
    driver.implicitly_wait(5)  # seconds
    driver.maximize_window()
    driver.get(PROPERTY_FORM_URL)
    elems = driver.find_elements(By.CSS_SELECTOR, '[role="listitem"]')
    elems[0].find_element(By.TAG_NAME, 'input').send_keys(a)
    elems[1].find_element(By.TAG_NAME, 'input').send_keys(p)
    elems[2].find_element(By.TAG_NAME, 'input').send_keys(l)
    driver.find_element(By.XPATH, '//form/div[2]/div/div[3]/div[1]/div[1]/div').click()
    # sleep(30000)
    driver.quit()


headers = {
    "Accept-Language":'en-US,en;q=0.9',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
res = req.get(zillow_url, headers=headers)
zillow_webpage = res.text
soup = BeautifulSoup(zillow_webpage, "html.parser")
cards = soup.select('div.list-card-info')
# Scrape the results from zillow
card_data = [
    {
        "address": card.find(class_='list-card-addr').get_text(),
        "price": card.find(class_='list-card-price').get_text(),
        "link": card.find(class_='list-card-link').get('href') if "https://www.zillow.com" in card.find(class_='list-card-link').get('href') else "https://www.zillow.com" + card.find(class_='list-card-link').get('href')
    }for card in cards if card.find(class_='list-card-addr') is not None
]
for data in card_data:
    save_listing(data["address"], data["price"].split('+')[0], data["link"])


