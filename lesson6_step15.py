from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем необходимую страницу
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Заполняем текстовые поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Alex")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Yankovky")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("example@gmail.com")
    # Загружаем txt фаил
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    # Нажимаем кнопку submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
finally:    
    time.sleep(10)
    browser.quit()