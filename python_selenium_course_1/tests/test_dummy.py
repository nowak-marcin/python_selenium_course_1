import time
import pytest
from python_selenium_course_1.conftest import init_driver
from python_selenium_course_1.src.helpers.config_helpers import get_base_url


@pytest.mark.usefixtures("init_driver")
class TestDummy:

    def test_dummy_func(self):
        url = get_base_url()
        self.driver.get(url)
        time.sleep(5)
        assert 'Demo eCom Store' in self.driver.title, 'incorrect page title'
        print(self.driver.title)
        print('test kontrolny 1')
        print('test kontrolny 2')
