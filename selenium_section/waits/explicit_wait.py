from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('file:///C:/Users/nowak/Desktop/qa_auto_learn/python_selenium_course_1/selenium_section/waits/page_with_slow_image.html')

my_image = wait.until(EC.visibility_of_element_located((By.ID, 'the_slow_image')))
print('znalazlem obrazek')
driver.quit()