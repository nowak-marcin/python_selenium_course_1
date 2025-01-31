from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'file:///C:/Users/marcinnowak/OneDrive%20-%20intive/Desktop/qa_automation_learning/python_selenium_course_1/selenium_section/elements2/radios_example.html'
driver.get(url)

expected_default_value = '21-40'
locator_by_value = 'input[name="age-group-radio"][value="{value}"]'

# ex1 - verify default is selected:
default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value=expected_default_value))
assert default_element.is_selected(), 'domyslny select 21-40 nie jest zaznaczony'
print('domyslny select 21-40 jest zaznaczony')

# ex2 -
expected_values = ['21-40', '41-60', '61-80', '81+', '39495']
all_radios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(all_radios) == len(expected_values), 'liczba radiobuttonow sie nie zgadza: ' \
    'oczekiwana: {}, aktualna: {}'.format(len(all_radios), len(expected_values))

driver.quit()


# The format() method formats the specified value(s) and insert them inside the string's placeholder{}.
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))