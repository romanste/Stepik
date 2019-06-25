from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

import math

x_element = browser.find_element_by_css_selector("#treasure")
x = x_element.get_attribute("valuex")
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)


input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)


option1 = browser.find_element_by_css_selector('#robotCheckbox')
option1.click()
option2 = browser.find_element_by_css_selector('#robotsRule')
option2.click()
button = browser.find_element_by_css_selector('button,submit')
button.click()
