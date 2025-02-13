import pytest


class TestBase:
    @pytest.mark.parametrize('num, result', [(1,11), (2,22), (3,33)])
    def test_calculation(self, num, result):
        assert 11*num == result
        print('wynik mnozenia jest rowny podanemu wynikowi')

    @pytest.mark.parametrize('user, password',
                        [('admin123@gmail.com', 'admin123'),
                         ('admin456@gmail.com', 'admin456')]
                         )
    def test_login_1_2(self, user, password):
        print (f'zaloguj danymi 2x')
