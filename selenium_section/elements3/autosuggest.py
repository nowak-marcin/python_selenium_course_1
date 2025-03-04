import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutoSuggestDropdown:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.lot.com/pl/pl')
        self.driver.maximize_window()
        time.sleep(5)

    def from_full_name_of_city(self, full_name):
        depart_from = self.driver.find_element(By.CSS_SELECTOR, "div[class='airport-select__value']")
        depart_from.click()
        time.sleep(5)
        input_from = self.driver.find_element(By.ID, "airport-select-0_combobox")
        input_from.send_keys(full_name)
        time.sleep(5)
        input_from.send_keys(Keys.ENTER)
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()
        print('test OK')


autosuggest1 = AutoSuggestDropdown()
autosuggest1.from_full_name_of_city('Szczecin')
autosuggest1.close_browser()
