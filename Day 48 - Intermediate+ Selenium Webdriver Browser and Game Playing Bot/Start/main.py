from selenium import webdriver
from selenium.webdriver.common.by import By
from env import *

driver = SELENIUM_BROWSER("chrome")

driver.get('http://www.python.org')
elems = driver.find_elements(by=By.CSS_SELECTOR, value="div.event-widget .menu li")
final_dict = {
    i: {
        "time": elems[i].find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0],
        "name": elems[i].find_element(By.TAG_NAME, 'a').get_attribute('innerText')
    } for i in range(len(elems))
}
driver.quit()
