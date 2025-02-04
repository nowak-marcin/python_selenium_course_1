import pytest


@pytest.mark.usefixtures("init_driver")
class TestDummy():

    def test_dummy_func(self):
        print('test kontrolny 1')
        print('test kontrolny 2')