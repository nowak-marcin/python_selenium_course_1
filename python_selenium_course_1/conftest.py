import pytest
from selenium import webdriver
# import os

#====driver initialization====

@pytest.fixture(scope="class")
def init_driver(request):
    # before all tests in class (setup):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    # after all tests in class (teardown):
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


#====pytest-html====

# <to do>:
# html_report
# screenshots