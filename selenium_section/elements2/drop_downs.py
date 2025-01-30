import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

url = 'file:///C:/Users/marcinnowak/OneDrive%20-%20intive/Desktop/qa_automation_learning/python_selenium_course_1/selenium_section/elements2/drop_down_example.html'

driver.get(url)
my_dropdown = driver.find_element('id', 'age-range-select')

# example 1 - 'Select class' import (tylko dla typowych dropdown):
dropdown_object = Select(my_dropdown)
dropdown_object.select_by_index(1)
time.sleep(5)
dropdown_object.select_by_value('21-40')
time.sleep(5)


# example 2 - niby select ale tak na prawde to button (trzeba najpierw kliknac)
dropdown_btn = driver.find_element('id', 'dropdownMenuButton')
dropdown_btn.click()

my_option = driver.find_element('xpath', '//*[@id="dropdowns"]/div[2]/div/ul/li[2]/a')
my_option.click()
time.sleep(5)

driver.quit()