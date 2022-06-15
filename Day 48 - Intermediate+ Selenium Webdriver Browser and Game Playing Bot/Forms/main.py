from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from env import *

driver = SELENIUM_BROWSER("chrome")
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_elem = driver.find_element(By.NAME, "fName").send_keys("Dickie")
last_name_elem = driver.find_element(By.NAME, "lName").send_keys("Lierman")
email_elem = driver.find_element(By.NAME, "email").send_keys("my@email.com")
signup_btn_elem = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

if driver.find_element(By.CSS_SELECTOR, ".jumbotron h1.display-3").text == 'Success!':
    print('Success!')


