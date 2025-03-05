import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutoSuggestDropdown:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://rozklad-pkp.pl/')
        self.driver.maximize_window()
        time.sleep(7)

    def start_full_name_of_city(self, full_name):
        input_from = self.driver.find_element(By.ID, 'from-station')
        input_from.click()
        input_from.send_keys(full_name)
        time.sleep(5)
        input_from.send_keys(Keys.ENTER)
        time.sleep(5)

    def end_list_of_cities(self, part_name):
        input_to = self.driver.find_element(By.ID, 'to-station')
        self.driver.execute_script("arguments[0].scrollIntoView(true)", input_to)
        input_to.click()
        time.sleep(5)
        input_to.send_keys(part_name)
        time.sleep(5)
        results = self.driver.find_elements(By.TAG_NAME, "li")
        for result in results:
            if 'Szczecin Podjuchy' in result.text:
                result.click()
                time.sleep(5)
                break
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()
        print('test OK')


autosuggest1 = AutoSuggestDropdown()
autosuggest1.start_full_name_of_city('Szczecin Główny')
autosuggest1.end_list_of_cities('Szczecin')
autosuggest1.close_browser()
