import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x1 = browser.find_element(By.ID, 'num1').text
    x2 = browser.find_element(By.ID, 'num2').text
    select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_value(str(int(x1) + int(x2)))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(6)
    browser.quit()
