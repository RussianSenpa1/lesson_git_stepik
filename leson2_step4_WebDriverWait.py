import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(r'D:\pythonProject\UchAvtoTest\cromedriver\chromedriver.exe')
    browser.implicitly_wait(5)      #неявное ожидание

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 15).until(      #явное ожидание (тут по тексту в элементе)
        EC.text_to_be_present_in_element((By.ID,'price'),'$100'))

    browser.find_element_by_id('book').click()

    x = int(browser.find_element_by_id('input_value').text)
    summ = calc(x)

    inputsum = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", inputsum)
    inputsum.send_keys(str(summ))

    button = browser.find_element_by_css_selector('[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
