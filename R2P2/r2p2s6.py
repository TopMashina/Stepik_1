import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    ans = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, 'answer').send_keys(ans)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]').click()
    button.click()

finally:
    time.sleep(6)
    browser.quit()
