# 'switch to frame' use:
# findElement, ID, NAME, INDEX


from selenium import webdriver

driver = webdriver.Chrome()

url = 'file:///C:/Users/nowak/Desktop/qa_auto_learn/python_selenium_course_1/selenium_section/iFrames/iFrames_example.html'

driver.get(url)

# ex.1 - button poza iframe:
driver.find_element('id', 'btnOutFrame').click()
my_alert = driver.switch_to.alert
my_alert_text = my_alert.text
assert my_alert_text == 'Just Clicked Outside iFrame', 'unexepcted text in alert'
print(my_alert_text)
my_alert.dismiss()


# ex.2 - button w iframe:
my_frame = driver.find_element('id', 'myFrame1')
driver.switch_to.frame(my_frame)
# lub:
# driver.switch_to.frame('myFrame1') --- dla ID lub NAME
# driver.switch_to.frame(0) --- INDEX - przelaczenie na pierwszy iframe od gory dokumentu

driver.find_element('id', 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

driver.switch_to.default_content()  # powrot do glownego dokumentu
driver.quit()
