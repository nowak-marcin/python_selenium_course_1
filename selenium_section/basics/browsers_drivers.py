# instalacja selenium:
# python -m pip install selenium

# instalacja chromedriver i zmienne srodowiskowe:
# https://jaktestowac.pl/lesson/pt1-mk1-02-przygotowanie-srodowiska/
# https://developer.chrome.com/docs/chromedriver/downloads?hl=pl
# https://knowledge.curiositysoftware.ie/docs/how-to-install-chromedriver-for-web-ui-testing

# import i inicalizacja webdriver (opcja1):

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# se = Service(executable_path='/.../.../.../chromedriver')
# driver = webdriver.Chrome(service=se)

# dodanie zmiennej srodowiskowej (najlepsza opcja):
# dodajemy sciezke do katalogu, w ktorym jest webdriver (windows -> zmienne srodowiskowe)

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/')
time.sleep(5)

driver.quit()
print('smoke test OK')
