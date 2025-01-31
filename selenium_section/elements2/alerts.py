# 1) html alert -> zwykly element strony (np zolta ramka z tekstem)
# 2) javascript alert -> pop up z OK
# 3) confirm alert -> pop up z OK/Cancel, moz byc dodatkowy komunikat
# 4) prompt alert -> pop up z inputem oraz OK/Cancel, moze byc dodatkowy komunikat
# 5) alert -> accept/dismiss

from selenium import webdriver

driver = webdriver.Chrome()

url = 'file:///C:/Users/marcinnowak/OneDrive%20-%20intive/Desktop/qa_automation_learning/python_selenium_course_1/selenium_section/elements2/alerts_example.html'
driver.get(url)

# ad.2):
alert_1_btn = driver.find_element('css selector', '#jsAlertExample > button')
alert_1_btn.click()

my_alert = driver.switch_to.alert
assert my_alert.text == 'I am a JavaScript Alert', 'niepoprawny komunikat w alercie'
my_alert.accept()

# ad.3):
my_js_confirm_btn = driver.find_element('css selector', '#jsConfirmExample > button')
my_js_confirm_btn.click()

my_confirm_alert = driver.switch_to.alert
my_confirm_alert.accept()

my_message = driver.find_element('id', 'userResponse1').text
assert my_message == 'Great! You will love it!', 'nieprawidlowa informacja dla usera'

# ad.4):
my_prompt_btn = driver.find_element('css selector', '#jsPromptExample > button')
my_prompt_btn.click()
my_prompt_alert = driver.switch_to.alert

input_name = 'janusz'
my_prompt_alert.send_keys(input_name)
my_prompt_alert.accept()

my_message2 = driver.find_element('id', 'userResponse2').text
assert my_message2 == f'You have entered: {input_name}', 'niepoprawny komunikat'

driver.quit()
