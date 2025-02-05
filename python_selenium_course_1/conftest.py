import pytest
from selenium import webdriver
# import os


@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()

    request.cls.driver = driver
    yield
    driver.quit()


#   supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff']

#   browser = os.environ.get('BROWSER', None)
#   if not browser:
#       raise Exception('zmienna srodowiskowa jest obowiazkowa')

#   browser = browser.lower()
#   if browser not in supported_browsers:
#       raise Exception('ta przegladarka nie jest obslugiwana')

#   if browser in ('chrome', 'ch'):
#       driver = webdriver.Chrome()
#   elif browser in ('firefox', 'ff'):
#       driver = webdriver.Firefox()
