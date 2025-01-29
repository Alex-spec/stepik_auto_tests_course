from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    sum_result = num1 + num2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_result)) 
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
    
finally:
    time.sleep(15)
    browser.quit()     
     