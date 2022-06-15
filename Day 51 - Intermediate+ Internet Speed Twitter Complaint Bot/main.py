from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from env import *
from time import sleep


class TwitterBot:
    def __init__(self):
        self.driver = SELENIUM_BROWSER("chrome")
        self.driver.implicitly_wait(60 * 2)  # seconds
        self.driver.maximize_window()

    def average_loss(self, speeds):
        down_speed = speeds[0]
        up_speed = speeds[0]
        loss1 = (1000 - down_speed) / 1000 * 100
        loss2 = (1000 - up_speed) / 1000 * 100
        average_loss = (loss1 + loss2) / 2
        speeds.append(average_loss)
        return speeds

    def get_speeds(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME, 'js-start-test').click()
        self.driver.find_element(By.LINK_TEXT, 'Back to test results').click()
        download_time = self.driver.find_element(By.CSS_SELECTOR, '[title="Receiving Time"]>.result-data span').text
        upload_time = self.driver.find_element(By.CSS_SELECTOR, '[title="Sending Time"]>.result-data span').text
        return [float(download_time), float(upload_time)]

    def post_to_twitter(self, speeds):
        self.driver.get("https://www.twitter.com/")
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="/login"]'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '[href="/login"]').click()
        username  = self.driver.find_element(By.CSS_SELECTOR, '[autocomplete="username"]')
        username.send_keys(TWITTER_USER)
        username.send_keys(Keys.ENTER)
        password = self.driver.find_element(By.CSS_SELECTOR, '[autocomplete="current-password"]')
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, '[data-text="true"]').send_keys(f"@EPB_Chattanooga, I'm getting speeds of {speeds[0]}/{speeds[1]} Mbps when I'm paying for 1000/1000 Mbps. Will I get {round(speeds[2], 2)}% off my bill, or do I just get {round(speeds[2], 2)}% off my service?")
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]').click()

    def run(self):
        speeds = self.get_speeds()
        speeds_and_average_loss = self.average_loss(speeds)
        if speeds_and_average_loss[2] > 5:
            self.post_to_twitter(speeds_and_average_loss)

    def run_starbucks(self):
        self.driver.get("https://www.twitter.com/")
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="/login"]'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '[href="/login"]').click()
        username = self.driver.find_element(By.CSS_SELECTOR, '[autocomplete="username"]')
        username.send_keys(TWITTER_USER)
        username.send_keys(Keys.ENTER)
        password = self.driver.find_element(By.CSS_SELECTOR, '[autocomplete="current-password"]')
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, '[data-text="true"]').send_keys(f"@Starbucks still doesn't care about their employees enough to let customers give a tip via a credit/debit card at the window/counter. \n\nI shouldn't have to download your app in order to show appreciation to your employees. \n\nFix this problem with your point of service system!")
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]').click()
bot = TwitterBot()
# bot.run()
bot.run_starbucks()
