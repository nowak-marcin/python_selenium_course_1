from selenium.webdriver.common.by import By


class MyAccountSignedOutLocator:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_USER_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[value="Log in"]')

    ERROR_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')
