import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Calendar:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://rozklad-pkp.pl/')
        self.driver.maximize_window()
        time.sleep(7)

    def select_calendar(self):
        calendar_field = self.driver.find_element(By.CSS_SELECTOR, '.data-filed')
        calendar_field.click()
        time.sleep(5)

    def select_current_date(self):
        current_day = self.driver.find_element(By.CSS_SELECTOR, ".ui-state-default.ui-state-highlight.ui-state-active")
        current_day.click()
        time.sleep(5)
        confirm_date_btn = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default pick-date']")
        confirm_date_btn.click()
        time.sleep(5)

    def select_day_in_next_month(self, random_day):
        next_month_btn = self.driver.find_element(By.CSS_SELECTOR, "a[title='Następny>']")
        next_month_btn.click()
        time.sleep(5)
        all_days = self.driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")
        # (By.CLASS_NAME, "ui-state-default")
        for day in all_days:
            if day.text == random_day:
                day.click()
                time.sleep(5)
                break
        time.sleep(5)
        confirm_date_btn = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default pick-date']")
        confirm_date_btn.click()
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()
        print('test OK')


test1 = Calendar()
test1.select_calendar()
test1.select_current_date()
test1.close_browser()

test2 = Calendar()
test2.select_calendar()
test2.select_day_in_next_month('4')
test2.close_browser()
