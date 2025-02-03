from selenium import webdriver
from selenium.webdriver.common.by import By


class InvalidUserLoginError:

    url = 'http://demostore.supersqa.com/my-account/'
    invalid_email = 'fjfjdff@supersqa.com'
    expected_message = 'Unknown email address. Check again or try your username.'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field1 = self.driver.find_element(By.ID, 'username')
        field1.send_keys(self.invalid_email)

    def input_password(self):
        field2 = self.driver.find_element(By.ID, 'password')
        field2.send_keys('acbe9837!')

    def click_login(self):
        self.driver.find_element(By.NAME, 'login').click()

    def verify_error_message(self):
        err_message = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_message = err_message.text
        assert displayed_message == self.expected_message, 'Dispalayed message is not expected'
        print('PASS')

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_message()
        self.driver.quit()


if __name__ == '__main__':

    obj = InvalidUserLoginError()
    obj.main()