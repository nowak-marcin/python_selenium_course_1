from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = 'file:///C:/Users/nowak/Desktop/qa_auto_learn/python_selenium_course_1/selenium_section/elements/present_vs_displayed.html'

driver.get(url)

my_btn1 = driver.find_element('id', 'btn1')
my_btn1_txt = my_btn1.text
print(f'tekst w przycisku 1 to: {my_btn1_txt}')

my_btn4 = driver.find_element('id', 'btn4')

if my_btn4.is_displayed():
    my_btn4_txt = my_btn4.text
    print(f'tekst w przycisku 4 to: {my_btn4_txt}')
    my_btn4.click()
else:
    raise Exception('przycisk jest niewidoczny!')

driver.quit()