from soft_assert import check, verify
import softest


# 1) module soft-assert - do not work!

def test_strong_assert(a):
    assert a.startswith("H"), f'{a} nie zaczyna się od H'
    print(f'{a} zaczyna sie od H')


# in this case scrip stops on 'start' with 'assertion error',
# does not check options after error ('Hey', 'Hola'):
#test_strong_assert('Hello')
#test_strong_assert('Hi')
#test_strong_assert('start')
#test_strong_assert('Hey')
#test_strong_assert('Hola')


def soft_assert(a):
    with verify():
        check(a.startswith("H"), f'{a} nie zaczyna się od H')
    print(f'{a} zaczyna sie od H')


soft_assert('Hello')
soft_assert('start')
soft_assert('Hey')
soft_assert('Hola')


# 2) softest module - do not work!

# class TestExample(softest.TestCase):

#   def test_soft_assertions(self):

        # Miękkie asercje
        #self.soft_assert(self.assertEqual,1 + 1, 3, "Suma nie jest poprawna")
        #self.soft_assert(self.assertEqual,"tekst", "inny tekst", "Porównanie tekstów")
        #self.soft_assert(self.assertTrue, 5 < 3, "Porównanie wartości")

        # Zakończenie testu i zgłoszenie błędów, jeśli występują
        #self.assert_all()


# 3) module pytest-soft-assertions with '--soft-assert' flag - do not work!

