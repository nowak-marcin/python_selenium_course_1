from python_selenium_course_1.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from python_selenium_course_1.src.SeleniumExtended import SeleniumExtended
from python_selenium_course_1.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.SeleniumExtended = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f'wchodzisz na strone: {my_account_url}')
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.SeleniumExtended.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.SeleniumExtended.wait_and_input_text(self.LOGIN_USER_PASSWORD, password)

    def click_login_button(self):
        logger.info('klikasz w login button')
        self.SeleniumExtended.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, expected_err):
        self.SeleniumExtended.wait_until_element_contains_text(self.ERROR_UL, expected_err)

    def input_register_email(self, email):
        self.SeleniumExtended.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.SeleniumExtended.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.info('klikasz w register button')
        self.SeleniumExtended.wait_and_click(self.REGISTER_BTN)