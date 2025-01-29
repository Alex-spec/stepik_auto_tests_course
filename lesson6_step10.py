from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Вычисляем математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2) 
    # Считываем значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(x)
    # Вводим ответ в текстовое поле 
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    time.sleep(1)
    # Отмечаем чекбокс I am robot
    checkbox_element = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox_element.click()
    time.sleep(1)
    # Выбираем radiobutton Robot rule!
    robot_element = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_element.click()
    time.sleep(1)
    # Нажимаем кнопку Submit
    submit_element = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_element.click()
    time.sleep(3)
finally:
    browser.quit()