from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fillName = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    fillName.send_keys("Ivan")
    fillSecondName = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    fillSecondName.send_keys("Petrov")
    fillEmail = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    fillEmail.send_keys("test@test.test")

    filelement = browser.find_element(By.CSS_SELECTOR, "[id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt') 
    filelement.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
