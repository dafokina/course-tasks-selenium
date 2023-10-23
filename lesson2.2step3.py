from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    x1 = number1.text

    number2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    x2 = number2.text

    x1 = int(x1) 
    x2 = int(x2) 

    def sum(x1, x2):
        return str(x1 + x2)
    
    result = str(x1 + x2)

    openList = browser.find_element(By.CSS_SELECTOR, "[id='dropdown']")
    openList.click()
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(result))

    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()