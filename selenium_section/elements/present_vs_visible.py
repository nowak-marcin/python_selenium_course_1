from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

url = 'file:///C:/Users/nowak/Desktop/qa_auto_learn/python_selenium_course_1/selenium_section/elements/present_vs_visible_example_with_cars.html'
driver.get(url)

bmw = driver.find_element(By.ID, 'bmw')
bmw.click()

bmw_series6 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))
bmw_series6.click()
print('bmw seria 6 jest widoczny do wyboru i można go wybrac')

driver.quit()