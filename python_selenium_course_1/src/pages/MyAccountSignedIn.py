from python_selenium_course_1.src.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator
from python_selenium_course_1.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocator):

    def __init__(self, driver):
        self.driver = driver
        self.SeleniumExtended = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.SeleniumExtended.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)




