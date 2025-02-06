from python_selenium_course_1.src.SeleniumExtended import SeleniumExtended
from python_selenium_course_1.src.pages.locators.HeaderLocator import HeaderLocator


class Header(HeaderLocator):
    def __init__(self, driver):
        self.driver = driver
        self.SeleniumExtended = SeleniumExtended(self.driver)

    def clik_on_cart_on_right_header(self):
        self.SeleniumExtended.wait_and_click(self.CART_RIGHT_HEADER)

    def wait_until_cart_item_count(self, count):
        expected_text = str(count) + ' item'
        self.SeleniumExtended.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)





