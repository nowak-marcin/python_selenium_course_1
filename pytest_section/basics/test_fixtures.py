import pytest


# @pytest.fixture(autouse=True, scope='class')
@pytest.fixture(scope='session')
def set_up():
    # before test:
    print('otworz przegladarke')
    print('wejdz na adres')
    print('zaloguj sie podanymi danymi')
    print('wejdz w zakladke z produktami')
    # after test (teardown):
    yield
    print('wyloguj się')
    print('zamknij przegladarke')


# 2 sposoby wywolania fixture o nazwie 'set_up':

@pytest.mark.usefixtures('set_up')
def test_add_new_product():
    print('produkt dodany poprawnie')

def test_remove_product(set_up):
    print('produkt usuniety poprawnie')


# scope=class -> the fixture is destroyed during teardown of the last test in the class
# scope=function -> the default scope, the fixture is destroyed at the end of every tests
# scope=session -> the fixture is destroyed at the end of the test session
