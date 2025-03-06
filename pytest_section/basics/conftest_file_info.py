# conftest means configuration of the test case initial - pre- and post-conditions at one place

#====configuration in conftest.py====

# @pytest.fixture()
# def tc_setup():
#   <go to url> ---> before test
#   <login to page> ---> before test
#   yield
#   <logout from page> ---> after test
#   <close browser> ---> after test

#====using in test====

# @pytest.mark.usefixtures("tc_setup")
# def add_product()
#   <select 1 product in cart>
#   <confirm your select>
#   <check if product exists in basket>

# def remove_product("tc_setup") -> the same as usefixtures
#   <select 1 product in basket>
#   <remove product>
#   <check if product doesn't exist in basket>

#====import for fixtures====

# from (...).conftest import tc_setup ---> ???

