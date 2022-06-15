from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from env import *
import time
driver = SELENIUM_BROWSER("chrome")
driver.get("http://orteil.dashnet.org/experiments/cookie/")
clicking = True
start = time.time()
end_time = start + (60 * 5)
while clicking:
    driver.find_element(By.ID, "cookie").click()
    check = time.time()
    if check - start > 5:
        available_purchases = [store for store in driver.find_elements(By.CSS_SELECTOR, '#rightPanel #store>div') if store.get_attribute('class') != 'grayed']
        if available_purchases:
            if len(available_purchases) > 1:
                available_purchases[-1].click()
        start = check
        if start > end_time:
            clicking = False
            print(driver.find_element(By.ID, "cps").text.split(': ')[1])
