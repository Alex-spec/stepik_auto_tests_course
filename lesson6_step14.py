from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Вычисляем математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # Скроллим страницу вниз и вводим ответ в поле
    input1 = browser.find_element(By.ID, 'answer')
    browser.execute_script("window.scrollBy(0, 150);")
    input1.send_keys(y)
    # Отмечаем чекбокс I am robot
    checkbox_element = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox_element.click()
    # Выбираем radiobutton Robot rule!
    robot_element = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_element.click()
    # Нажимаем кнопку Submit
    submit_element = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_element.click()
    time.sleep(5)
finally:
    browser.quit()