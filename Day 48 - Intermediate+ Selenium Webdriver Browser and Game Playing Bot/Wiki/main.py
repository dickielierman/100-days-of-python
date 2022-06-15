from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from env import *

driver = SELENIUM_BROWSER("chrome")

driver.get('https://en.wikipedia.org/wiki/Main_Page')
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
search_bar = driver.find_element(By.ID, "searchInput")
search_bar.send_keys('Python')
search_bar.send_keys(Keys.ENTER)
print(article_count.text)

# driver.quit()
