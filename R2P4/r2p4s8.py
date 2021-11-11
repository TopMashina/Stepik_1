import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'h5#price'), '100'))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    x = browser.find_element(By.ID, 'input_value').text
    ans = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, 'answer').send_keys(ans)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(6)
    browser.quit()
