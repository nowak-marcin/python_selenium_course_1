import pytest
from python_selenium_course_1.conftest import init_driver
from python_selenium_course_1.src.pages.HomePage import HomePage
from python_selenium_course_1.src.pages.Header import Header
from python_selenium_course_1.src.pages.CartPage import CartPage
from python_selenium_course_1.src.configs.generic_configs import GenericConfigs
from python_selenium_course_1.src.pages.CheckoutPage import CheckoutPage
from python_selenium_course_1.src.pages.OrderReceivedPage import OrderReceivedPage


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:

    def test_end_to_end_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)

        # wejscie na strone glowna:
        home_p.go_to_home_page()

        # dodaj pierwszy dowolny product:
        home_p.click_first_add_to_cart_button()

        # poczekaj, az w prawym panelu pojawi sie '1 item' i kliknij:
        header.wait_until_cart_item_count(1)
        header.clik_on_cart_on_right_header()

        # pobierz produkt:
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, 'na liscie nie ma produktow lub sa wiecej niz jeden...'

        # podaj kupon znizkowy:
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        # zatwierdz zamowienie:
        cart_p.click_on_proceed_to_checkout()

        # wypelnij formularz danymi:
        checkout_p.fill_in_billing_info()

        # wyslij zlecenie do realizacji (click place order):
        checkout_p.click_place_order()

        # sprawdz czy otworzyla sie strona z potwierdzeniem: 
        order_received_p.verify_order_received_page_loaded()

        # pobranie numeru orderu:
        order_no = order_received_p.get_order_number()
        print(f'===***{order_no}***===')

        # verify order is recorder in db (via sql or api)