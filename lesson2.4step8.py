from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']")
button.click()
 
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)

sendAnswer = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
sendAnswer.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "[id='solve']")
button.click()

time.sleep(20)
browser.quit()