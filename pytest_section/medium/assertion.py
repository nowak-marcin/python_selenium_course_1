from soft_assert import check, verify

def strong_assert(a):
    assert a.startswith("H"), f'{a} nie zaczyna się od H'
    print(f'{a} zaczyna sie od H')


# in this case scrip stops on 'start' with 'assertion error',
# does not check options after error ('Hey', 'Hola'):
#strong_assert('Hello')
#strong_assert('start')
#strong_assert('Hey')
#strong_assert('Hola')


def soft_assert(a):
    with verify():
        check(a.startswith("H"), f'{a} nie zaczyna się od H')
    print(f'{a} zaczyna sie od H')


soft_assert('Hello')
soft_assert('start')
soft_assert('Hey')
soft_assert('Hola')
print('koniec')












