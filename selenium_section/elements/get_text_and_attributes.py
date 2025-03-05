import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://koleo.pl/')
driver.maximize_window()
time.sleep(5)

my_element1 = driver.find_element('css selector', "h2[class='show-for-medium-up']")
my_element2 = driver.find_element('id', 'small_search')
print(my_element1.text, my_element2.text)

my_list_texts = [my_element1.text, my_element2.text]
if 'Wyszukaj połączenie i kup bilet!' in my_list_texts:
    print('text1 is OK')
if 'ZNAJDŹ POŁĄCZENIE' in my_list_texts:
    print('text2 is OK')
else:
    print('wrong text in text field...')

my_element3 = driver.find_element('id','query_date')
print(my_element3.get_attribute('placeholder'))
print(my_element3.get_attribute('type'))

driver.quit()
