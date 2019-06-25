from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

import math

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)


input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)
browser.execute_script("window.scrollBy(0, 100);")
option1 = browser.find_element_by_css_selector('#robotCheckbox')
option1.click()
option2 = browser.find_element_by_css_selector('#robotsRule')
option2.click()
button = browser.find_element_by_css_selector('button,submit')
button.click()
