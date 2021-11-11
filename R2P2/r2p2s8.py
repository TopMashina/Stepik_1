from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element(By.XPATH, '//label[text()="First name* "]/following::input').send_keys('Test')
    browser.find_element(By.XPATH, '//label[text()="Last name*"]/following::input').send_keys('Test')
    browser.find_element(By.XPATH, '//label[text()="Email * "]/following::input').send_keys('Test')
    browser.find_element(By.ID, 'file').send_keys('C:/Intel/cf-key.txt')
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(6)
    browser.quit()
