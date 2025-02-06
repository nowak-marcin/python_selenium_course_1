import pytest
from python_selenium_course_1.src.pages.MyAccountSignedOut import MyAccountSignedOut
from python_selenium_course_1.src.pages.MyAccountSignedIn import MyAccountSignedIn
from python_selenium_course_1.src.helpers.generic_helpers import generate_random_email_and_password
from python_selenium_course_1.conftest import init_driver


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)

        my_account_o.go_to_my_account()

        rand_email = generate_random_email_and_password()
        my_account_o.input_register_email(rand_email['email'])

        my_account_o.input_register_password('123000abc!')
        my_account_o.click_register_button()

        # sprawdzenie czy user jest zalogowaniu (widocznosc buttona log out):
        my_account_i.verify_user_is_signed_in()
