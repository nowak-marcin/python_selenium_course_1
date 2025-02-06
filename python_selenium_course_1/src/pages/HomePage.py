from python_selenium_course_1.src.helpers.config_helpers import get_base_url
from python_selenium_course_1.src.SeleniumExtended import SeleniumExtended
from python_selenium_course_1.src.pages.locators.HomePageLocator import HomePageLocator


class HomePage(HomePageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.SeleniumExtended = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.SeleniumExtended.wait_and_click(self.ADD_TO_CART_BUTTON)

