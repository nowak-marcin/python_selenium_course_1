import pytest


# pytestmark = [pytest.mark.regression, pytest.mark.smoke]

@pytest.mark.smoke
@pytest.mark.regression
def test_login_page_valid_user():
    print('log in with valid user')

@pytest.mark.regression
def test_login_with_wrong_password():
    print('log in with wrong password')


# terminal: pytest -m regression, pytest -m "smoke and regression"
# mozna tez ustawic kilka markerow dla jednego skryptu:
# pytestmark = [pytest.mark.regression, pytest.mark.smoke]

# obejscie warningow dla markerow:
# terminal: pytest --disable-warnings
# terminal: pytest -W ignore::pytest.PytestUnknownMarkWarning
# utworzenie config file z rejestracja markerow lub z wyklueczeniem warningow: pytest.ini
