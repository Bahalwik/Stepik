from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    my_func = calc(x)
    element = browser.find_element(By.ID, 'answer')
    element.send_keys(my_func)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
