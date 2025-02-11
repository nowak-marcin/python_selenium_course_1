import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'file:///C:/Users/nowak/Desktop/qa_auto_learn/python_selenium_course_1/selenium_section/elements2/checkbox_example.html'

driver = webdriver.Chrome()
driver.get(url)

# sposob1:
my_choice = driver.find_element(By.CSS_SELECTOR, '#checkboxes > div > input:nth-child(7)')
my_choice.click()
assert my_choice.is_selected(), f'opcja nie jest zaznaczona'
time.sleep(5)

# sposob2:
to_select_value = '21-40'
locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'

my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
my_choice.click()
assert my_choice.is_selected(), f'opcja nie jest zaznaczona'
time.sleep(5)

# sposob3 - weryfikacja ile jest checkboxów i czy są zaznaczone:
expected_number_of_options = 4

all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == expected_number_of_options, 'chekboxow jest za malo albo za duzo'

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f'checkbox z atrybutem {value} zostal zaznaczony')
    else:
        raise Exception(f'checkbox z atrybutem {value} nie zostal zaznaczony !!!')

time.sleep(5)
driver.quit()

# wynik testu prawidlowy - sposob3 wykonal odznaczenie '61-81', zaznaczonego w sposob1
