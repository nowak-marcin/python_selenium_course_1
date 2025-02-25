from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/')

# TAG_NAME (musi to byc tag <a>)
all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f'ilosc tagow o nazwie <a> to: {len(all_links)}')
for i in all_links:
    print(i.text)

# LINK_TEXT (musi to byc tag <a>)
account_elm = driver.find_element(By.LINK_TEXT, 'My account')
print('element znaleziony')
account_elm_2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')
print('element znaleziony')

driver.quit()