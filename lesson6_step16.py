from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Вычисляем математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
# Открываем страницу
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
# Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
# Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()
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