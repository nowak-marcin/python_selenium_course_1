import pytest
from python_selenium_course_1.src.pages.MyAccountSignedOut import MyAccountSignedOut
from python_selenium_course_1.conftest import init_driver


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    def test_login_none_existing_user(self):

        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('eioejfjfert')
        my_account.input_login_password('fjfjgjjg23!')
        my_account.click_login_button()

    # verify error message:
        expected_err = (f'Error: The username eioejfjfert is not registered on this site.'
                        f' If you are unsure of your username, try your email address instead.')
        my_account.wait_until_error_is_displayed(expected_err)