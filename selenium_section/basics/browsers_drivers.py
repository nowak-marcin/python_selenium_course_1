# instalacja selenium:
# python -m pip install selenium

# instalacja chromedriver i zmienne srodowiskowe:
# https://jaktestowac.pl/lesson/pt1-mk1-02-przygotowanie-srodowiska/
# https://developer.chrome.com/docs/chromedriver/downloads?hl=pl
# https://knowledge.curiositysoftware.ie/docs/how-to-install-chromedriver-for-web-ui-testing

# import i inicalizacja webdriver (opcja1):

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# se = Service(executable_path='C:\\...\\chromedriver.exe')
# driver = webdriver.Chrome(service=se)

# dodanie zmiennej srodowiskowej (najlepsza opcja):
# dodajemy sciezke do katalogu, w ktorym jest webdriver (windows -> zmienne srodowiskowe)

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/')
time.sleep(5)
driver.maximize_window()

time.sleep(5)
print(driver.title)

driver.quit()
print('smoke test OK')


# wersja z webdriver-manager:
# import webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('http://demostore.supersqa.com/')