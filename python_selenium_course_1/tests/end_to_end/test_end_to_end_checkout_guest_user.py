import pytest
from python_selenium_course_1.conftest import init_driver
from python_selenium_course_1.src.pages.HomePage import HomePage
from python_selenium_course_1.src.pages.Header import Header
from python_selenium_course_1.src.pages.CartPage import CartPage
from python_selenium_course_1.src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:

    def test_end_to_end_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)

        home_p.go_to_home_page()

        # dodaj pierwszy dowoolny product:
        home_p.click_first_add_to_cart_button()

        # poczekaj, az w prawym panelu pojawi sie '1 item' i kliknij:
        header.wait_until_cart_item_count(1)
        header.clik_on_cart_on_right_header()

        # pobierz produkty:
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, 'na liscie nie ma produktow lub sa wiecej niz jeden...'

        # podaj kupon znizkowy:
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)







        # apply free coupon "ssqa100"
        # select free shipping
        # click on checkout
        # fill in form
        # click on place order
        # verify order is received
        # verify order is recorder in db (via sql or api)