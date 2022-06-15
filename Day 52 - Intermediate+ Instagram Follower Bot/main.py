from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from env import *

searcher = 'pattonoswalt'


class InstagramBot:
    def __init__(self):
        self.driver = SELENIUM_BROWSER("chrome")
        self.driver.implicitly_wait(10)  # seconds
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        self.driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(INSTA_USER)
        self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(INSTA_PASS)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        sleep(8)
        self.driver.find_element(By.CSS_SELECTOR, '[role="main"]>div>div>div>div [type="button"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[role="dialog"] button + button').click()

    def run(self):
        # self.login()
        self.driver.get(f'https://www.instagram.com/{searcher}/following/')
        self.follow_following()
    def follow_following(self):
        total = 0
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'main section ul li:last-child a').click()
        sleep(2)
        scrolling=True
        while scrolling:
            buttons = [button for button in self.driver.find_elements(By.CSS_SELECTOR, '[role="dialog"] ul button') if button.text == 'Follow']
            while not buttons:
                bottom = self.driver.find_element(By.CSS_SELECTOR, '[role="dialog"] ul+div')
                self.driver.execute_script("arguments[0].scrollIntoView();", bottom)
                sleep(1)
                buttons = [button for button in self.driver.find_elements(By.CSS_SELECTOR, '[role="dialog"] ul button') if button.text == 'Follow']
            for button in buttons:
                self.driver.execute_script("arguments[0].scrollIntoView();", button)
                button.click()
                total += 1
                if total > 9:
                    scrolling = False
                sleep(1)


bot = InstagramBot()
bot.run()
