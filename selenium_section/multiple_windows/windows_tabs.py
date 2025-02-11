from selenium import webdriver

driver = webdriver.Chrome()

url = 'file:///C:/Users/nowak/Desktop/qa_auto_learn/python_selenium_course_1/selenium_section/multiple_windows/windows-and_tabs_example.html'
driver.get(url)

driver.find_element('xpath', '//*[@id="windows"]/a[1]').click()

print(f'obecny tutul strony to: {driver.title}')
all_window = driver.window_handles
main_window = all_window[0]
new_window = all_window[1]
driver.switch_to.window(new_window)
print(f'nowy tutul strony to: {driver.title}')

my_heading1 = driver.find_element('xpath', '/html/body/h1').text
print(my_heading1)

driver.close()
driver.switch_to.window(main_window)
print(f'zamknieto tab1, powrot do glowej strony z tytulem: {driver.title}')

driver.quit()
