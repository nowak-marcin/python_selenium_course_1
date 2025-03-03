import time
from selenium import webdriver


class JavaScriptDemo:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_url(self):
        self.driver.execute_script("window.open('http://demostore.supersqa.com', '_self');")
        time.sleep(5)
        page_url = str(self.driver.execute_script("return document.URL"))
        print(page_url)

    def get_page_title(self):
        page_title = str(self.driver.execute_script("return document.title"))
        print(page_title)

    def click_element(self):
        #console: document.getElementsByTagName('img')[0] (pierwszy obrazek na stronie)
        first_img = self.driver.execute_script("return document.getElementsByTagName('img')[0];")
        self.driver.execute_script("arguments[0].click();", first_img)
        time.sleep(5)
        # lub:
        # self.driver.execute_script("document.getElementsByTagName('img')[0].click()")

    def input_text(self):
        search_product = self.driver.execute_script("return document.getElementsByName('s')[0];")
        self.driver.execute_script("arguments[0].value='glasses'", search_product)
        time.sleep(5)

    def refresh_page(self):
        self.driver.execute_script("history.go(0)")
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()
        print('test OK')


js_demo_1 = JavaScriptDemo()

js_demo_1.open_url()
js_demo_1.get_page_title()
js_demo_1.click_element()
js_demo_1.input_text()
js_demo_1.refresh_page()
js_demo_1.close_browser()
