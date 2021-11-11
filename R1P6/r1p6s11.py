from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element(By.XPATH, '//label[text()="First name*"]/following::input').send_keys('Test')
    browser.find_element(By.XPATH, '//label[text()="Last name*"]/following::input').send_keys('Test')
    browser.find_element(By.XPATH, '//label[text()="Email*"]/following::input').send_keys('Test')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    assert "Congratulations! You have successfully registered!" == welcome_text_elt.text

finally:
    time.sleep(6)
    browser.quit()
