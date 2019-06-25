from selenium import webdriver
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
field1 = browser.find_element_by_css_selector('[name="firstname"]')
field1.send_keys("Ivan")
field2 = browser.find_element_by_css_selector('[name="lastname"]')
field2.send_keys("Govnov")
field3 = browser.find_element_by_css_selector('[name="email"]')
field3.send_keys("zalupenshtein@yopmail.com")

# make an <input type="file"> available
import os
browser.execute_script("""
    document.addEventListener('click', function(evt) {
    if (evt.target.type === 'file')
    evt.preventDefault();
    }, true)
    """)
current_dir = os.path.abspath(os.path.dirname('Documents/Script/'))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'text.txt')
browser.find_element_by_css_selector('[name="file"]')\
    .click()
# assign the file to the <input type="file">
browser.find_element_by_css_selector('input[type=file]')\
    .send_keys(file_path)
         # добавляем к этому пути имя файла
button = browser.find_element_by_css_selector('button[type=submit]')
button.click()
