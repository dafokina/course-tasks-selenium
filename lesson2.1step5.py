from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    number = x_element.get_attribute("valuex")
    #print("the number in the treasure is ", number)
    x = number
    y = calc(x)

    fillEmail = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    fillEmail.send_keys(y)

    fillCheckbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    fillCheckbox.click()

    fillRadioButton = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    fillRadioButton.click()

    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
