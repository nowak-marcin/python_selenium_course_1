import pytest


@pytest.fixture
def set_up():
    print('otworz przegladarke')
    print('wejdz na adres')
    print('zaloguj sie podanymi danymi')
    print('wejdz w zakladke z produktami')
    yield
    print('wyloguj się')
    print('zamknij przegladarke')


@pytest.mark.usefixtures('set_up')
def test_add_new_product():
    print('produkt dodany poprawnie')

@pytest.mark.usefixtures('set_up')
def test_remove_product():
    print('produkt usuniety poprawnie')