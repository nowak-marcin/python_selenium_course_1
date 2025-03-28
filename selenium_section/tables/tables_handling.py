import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# https://omayo.blogspot.com/

# xpath:
# - //table[@id='table1']/tbody/tr/td or //table[@id='table1']/tbody//td -> all data
# - //table[@id='table1']/thead/tr/th or //table[@id='table1']/thead//th
# - //table[@id='table1']/tbody/tr[1]/td -> only first row
# - //table[@id='table1']/tbody/tr[2]/td -> only second row
# - //table[@id='table1']/tbody/tr[3]/td[2] -> 3rd row in 2nd column

# - //table[@id='table1']/tbody/tr/td[1] -> only 1st column details
# - $x("//table[@id='table1']/tbody/tr/td[1]") -> console


class TableHandling:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://omayo.blogspot.com/')
        self.driver.maximize_window()
        time.sleep(5)

    def get_headings(self):
        headings = self.driver.find_elements(By.XPATH, "//table[@id='table1']/thead/tr/th")
        for heading in headings:
            print(heading.text)

    def all_data_from_body(self):
        all_data = self.driver.find_elements(By.XPATH, "//table[@id='table1']/tbody//td")
        for data in all_data:
            print(data.text)

    def data_per_row(self):
        first_row = self.driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")
        for data in first_row:
            print(data.text)

    def data_per_row_and_column(self):
        col3_row2 = (By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[2]")
        col2_row3 = "//table[@id='table1']/tbody/tr[2]/td[3]"

        data1 = self.driver.find_element(*col3_row2)
        data2 = self.driver.find_element(By.XPATH, col2_row3)
        print(data1.text, data2.text)

    def data_per_column(self):
        col1 = (By.XPATH, "//table[@id='table1']//tr//td[1]")
        col2 = (By.XPATH, "//table[@id='table1']/tbody/tr/td[2]")
        col1_data = self.driver.find_elements(*col1)
        col2_data = self.driver.find_elements(*col2)

        for data1 in col1_data:
            print(data1.text)
        for data2 in col2_data:
            print(data2.text)

    def close_browser(self):
        self.driver.quit()
        print('test OK')


test1 = TableHandling()
# test1.get_headings()
# test1.all_data_from_body()
# test1.data_per_row()
# test1.data_per_row_and_column()
test1.data_per_column()
test1.close_browser()
