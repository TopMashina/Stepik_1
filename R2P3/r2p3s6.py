import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    ans = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, 'answer').send_keys(ans)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(6)
    browser.quit()
