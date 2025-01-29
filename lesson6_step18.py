from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Вычисляем математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
# Открываем страницу
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
# говорим Selenium дождаться, когда цена дома уменьшится до $100
    WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), "$100" )
    )
    button = browser.find_element(By.ID, 'book')
    button.click()
# Вычисляем значение x для формулы   
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
# Вводим значение в инпут
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
# Сабмитим
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()