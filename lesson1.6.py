from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fillName = browser.find_element(By.CSS_SELECTOR, "div.first_block>.form-group.first_class:nth-child(1) input")
    fillName.send_keys("Ivan")
    fillSecondName = browser.find_element(By.CSS_SELECTOR, "div.first_block>.form-group.second_class:nth-child(2) input")
    fillSecondName.send_keys("Petrov")
    fillEmail = browser.find_element(By.CSS_SELECTOR, "div.first_block>.form-group.third_class:nth-child(3) input")
    fillEmail.send_keys("test@test.test")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
