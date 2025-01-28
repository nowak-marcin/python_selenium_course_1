# from selenium.webdriver.common.by import By
# find_element - zwraca pojedynczy webelement, find_elements - zwraca liste webelementów

# find_element(By.ID,'<locator>')
# find_element('xpath', '<locator>)

# my_table = driver.find_element(By.ID, 'mainTable')
# my_rows = my_table.find_elements('tag name', 'tr')


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ID:
driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/')

cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()
time.sleep(3)
driver.quit()

print('test OK')

# CSS_SELECTOR:
driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/')

cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart')
cart.click()
time.sleep(3)
driver.quit()

print('test OK')

# XPATH:
driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/')

cart = driver.find_element(By.XPATH, '//*[@id="site-header-cart"]')
cart.click()
time.sleep(3)
driver.quit()

print('test OK')
