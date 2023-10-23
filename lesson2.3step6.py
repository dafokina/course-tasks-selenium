from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])

    time.sleep(5)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    sendAnswer = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    sendAnswer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()