from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from env import *
from time import sleep

applied = 0


driver = SELENIUM_BROWSER("chrome")
driver.implicitly_wait(5) # seconds
driver.maximize_window()
driver.get("https://www.linkedin.com/")
driver.find_element(By.LINK_TEXT, 'Sign in').click()
driver.find_element(By.ID, 'username').send_keys(LINKEDIN_EMAIL)
driver.find_element(By.ID, 'password').send_keys(LINKEDIN_PASS)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
# Auth question possible
# try:
#     driver.find_element(By.CLASS_NAME, 'secondary-action').click()
#     # my_click('class', 'secondary-action')
# except:
#     pass
# Navigate to jobs
driver.find_element(By.CSS_SELECTOR, 'a[data-control-name="nav_jobs"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[data-control-name="job_searches_recent_search_click_0"]').click()
# Open job filters
driver.find_element(By.XPATH, '//button[text()="All filters"]').click()
# Set filters
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'div.artdeco-modal__actionbar .artdeco-button--muted').click()
driver.find_element(By.CSS_SELECTOR, '[for="advanced-filter-sortBy-R"]').click()
driver.find_element(By.CSS_SELECTOR, '[for="advanced-filter-timePostedRange-"]').click()
driver.find_element(By.CSS_SELECTOR, '[for="advanced-filter-experience-2"]').click()
driver.find_element(By.CSS_SELECTOR, '[for="advanced-filter-experience-4"]').click()
driver.find_element(By.CSS_SELECTOR, '[for="advanced-filter-jobType-F"]').click()
driver.find_element(By.CSS_SELECTOR, '[for="advanced-filter-jobType-C"]').click()
driver.find_element(By.CSS_SELECTOR, '[for="advanced-filter-workplaceType-2"]').click()
driver.find_element(By.XPATH, "//text()[. = 'Easy Apply filter']/../../div").click()
driver.find_element(By.CSS_SELECTOR, 'div.artdeco-modal__actionbar .artdeco-button--primary').click()
while applied < 20:
    sleep(2)
    available_jobs = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list>li')
    for job in available_jobs:
        job.click()
        sleep(1)
        if 'automation' in driver.find_element(By.CSS_SELECTOR, '.jobs-unified-top-card__job-title').text.lower() or 'test' in driver.find_element(By.CSS_SELECTOR, '.jobs-unified-top-card__job-title').text.lower():
            try:
                sleep(1)
                driver.implicitly_wait(2)
                driver.find_element(By.CSS_SELECTOR, '.jobs-unified-top-card__content--two-pane .jobs-apply-button--top-card .artdeco-button--primary').click()
                driver.implicitly_wait(5)
                driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__content .artdeco-button--primary').click()

                perc_complete = driver.find_element(By.CSS_SELECTOR, '.artdeco-completeness-meter-linear__progress-element').get_attribute('value')

                if int(perc_complete) < 50:
                    driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss').click()
                    driver.find_element(By.CSS_SELECTOR, '[data-control-name="discard_application_confirm_btn"]').click()
                else:
                    driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__content .artdeco-button--primary').click()
                    sleep(1)
                    driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__content .artdeco-button--primary').click()
                    applied += 1
                    print(f"Applied to {applied} job(s)")
            except:
                pass
    driver.find_element(By.CSS_SELECTOR, '.artdeco-pagination__pages li.active + li').click()
driver.quit()


