import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class JavaScriptScroll:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://omayo.blogspot.com/')
        self.driver.maximize_window()
        time.sleep(5)

    def scroll_to_element(self):
        dropdown_button = self.driver.find_element(By.CSS_SELECTOR, '.dropbtn')
        self.driver.execute_script("arguments[0].scrollIntoView(true)", dropdown_button)
        time.sleep(5)
        dropdown_button.click()
        time.sleep(5)

    def scroll_to_end_of_page(self):
        # console: document.documentElement.scrollHeight
        self.driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()
        print('test OK')


js_scroll = JavaScriptScroll()
js_scroll.scroll_to_element()
js_scroll.close_browser()

js_scroll2 = JavaScriptScroll()
js_scroll2.scroll_to_end_of_page()
js_scroll2.close_browser()
