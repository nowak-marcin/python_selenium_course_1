import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# login i haslo:

driver.get('http://demostore.supersqa.com/my-account/')

u_name = driver.find_element('id', 'username')
u_name.send_keys('abcde')

time.sleep(5)

p_field = driver.find_element('id', 'password')
p_field.send_keys('mypassword')

log_in_btn = driver.find_element('css selector', '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
log_in_btn.click()


# pole "szukaj" z lupka, bez buttona:

driver.get('http://demostore.supersqa.com/')

search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
search_field.click()
search_field.send_keys('Belt')
time.sleep(5)
search_field.send_keys(Keys.ENTER)


# przeskok na kolejnego taba:

driver.get('http://demostore.supersqa.com/my-account/')

u_name = driver.find_element('id', 'username')
u_name.send_keys('abcde')
time.sleep(5)
u_name.send_keys(Keys.TAB)

driver.quit()
