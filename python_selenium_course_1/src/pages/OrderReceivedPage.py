from python_selenium_course_1.src.SeleniumExtended import SeleniumExtended
from python_selenium_course_1.src.pages.locators.OrderReceivedPageLocator import OrderReceivedPageLocator


class OrderReceivedPage(OrderReceivedPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.SeleniumExtended = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.SeleniumExtended.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, 'Order received')

    def get_order_number(self):
        return self.SeleniumExtended.wait_and_get_text(self.ORDER_NUMBER)



