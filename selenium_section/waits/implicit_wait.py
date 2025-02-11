# pobranie adresu strony:
# prawy myszy -> kopiuj sciezke absolutna
# wklejenie w przegladarke
# pobranie adresu z paska adres w formacie file:///


from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('file:///C:/Users/nowak/Desktop/qa_auto_learn/python_selenium_course_1/selenium_section/waits/page_with_slow_image.html')

my_image = driver.find_element('id', 'the_slow_image')
print('znalazlem obrazek')
driver.quit()


