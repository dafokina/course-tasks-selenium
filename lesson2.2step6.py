from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    sendAnswer = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    sendAnswer.send_keys(y)

    fillCheckbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);",  fillCheckbox)
    fillCheckbox.click()

    fillRadioButton = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", fillRadioButton)
    fillRadioButton.click()

    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()