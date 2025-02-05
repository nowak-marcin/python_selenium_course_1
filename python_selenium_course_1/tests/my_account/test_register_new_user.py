import pytest


@pytest.fixture.usefixtures('init_driver')
class TestRegisterNewUser:

    def test_register_valid_new_user(self):

        # go to my account:
        # fill in email:
        # fill in password
        # click register
        # verify user is registered
