import pytest


@pytest.mark.regression
class TestCheckout:
    def test_checkout_as_guest(self):
        print('checkout guest')

    def test_checkout_existing_user(self):
        print('checkout existing user')


# terminal: pytest -vs
