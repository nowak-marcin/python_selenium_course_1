import pytest


# pytestmark = [pytest.mark.regression, pytest.mark.smoke]

@pytest.mark.smoke
@pytest.mark.regression
def test_login_page_valid_user():
    print('log in with valid user')

@pytest.mark.regression
def test_login_with_wrong_password():
    print('log in with wrong password')

@pytest.mark.skip(reason='not ready')
def test_case_in_progress_1():
    print('ten nic nie robi')

@pytest.mark.xfail
def test_case_in_progres_2():
    assert 4 + 2 == 5
print('tu jest blad')


# terminal: pytest --markers
# terminal: pytest -vsm regression, pytest -m "smoke and regression"
# mozna tez ustawic kilka markerow dla jednego skryptu:
# pytestmark = [pytest.mark.regression, pytest.mark.smoke]

# @pytest.mark.skip(reason=brak implementacji) - do pomijania testow
# @pytest.mark.xfail(condition, reason=in progres) - do pomijania testow ze znanym bledem

# obejscie warningow dla markerow:
# terminal: pytest --disable-warnings
# terminal: pytest -W ignore::pytest.PytestUnknownMarkWarning
# utworzenie config file z rejestracja markerow lub z wyklueczeniem warningow: pytest.ini
