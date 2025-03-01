from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, StaleElementReferenceException
import time


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)).click()

    # wait_and_click - zamiast 2x visibility_of_element... mozna dac element_to_be_clickable.

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text))

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else 'nie moge zlokalizowac elementu w wyznaczonym czasie'
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(err)

        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        element_text = element.text

        return element_text
