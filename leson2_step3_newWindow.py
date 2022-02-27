import math

from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(r'D:\pythonProject\UchAvtoTest\cromedriver\chromedriver.exe')
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)


    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id('input_value').text)
    summ = calc(x)

    inputsum = browser.find_element_by_id('answer').send_keys(str(summ))

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
