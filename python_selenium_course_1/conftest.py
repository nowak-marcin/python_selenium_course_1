import pytest
from selenium import webdriver
# import os


@pytest.fixture(scope="class")
def init_driver(request):
    # before test:
    driver = webdriver.Chrome()
    request.cls.driver = driver
    # after test (teardown):
    yield
    driver.quit()


# @pytest.fixture(params=['chrome', 'firefox'], scope='class')
# def init_driver(request):
#   if request.param == 'chrome':
#       driver = webdriver.Chrome()
#   if request.param == 'firefox':
#       driver = webdriver.Firefox()
#   request.cls.driver = driver
#   yield
#   diver.quit()

#   terminal: pytest -sv <plik.py> --browser chrome


#   ===========================pytest-html========================================
#   konfiguracja raportowania testow w html report
#   ustawienia na podstawie dokumentacji - hook
#   ustawienie generowania raportow i screenow tylko dla testow FE
