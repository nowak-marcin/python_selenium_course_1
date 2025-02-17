#   def my_first_function(parameters)
#       <code here>
#       return <something>

# Słowo kluczowe return powoduje opuszczenie funkcji (instrukcje umieszczone poniżej nie są wykonywane).
# Return pozwala również na przekazanie wartości z wnętrza funkcji do reszty programu
# parameters i return - sa opcjonalne
# zmienne w funkcji sa uzyte tylko lokalnie - w funkcji i jej wywolaniu
# jesli chcemy uzyc globalnie - global
# arguments - positional, required, optional, keyword


def my_adding_func(a, b, c=1):
    return a + b + c


def my_multi_func(a, b):
    if a != 0 and b != 0:
        multi = a * b
        return f'iloczyn liczb wynosi {multi}'
    else:
        return 'jedna z liczb to zero!'


value1 = my_adding_func(5, 10, c=5)
print(value1)
value2 = my_adding_func(5, b=5)
print(value2)
value3 = my_multi_func(3,5)
print(value3)
value4 = my_multi_func(0,2)
print(value4)


# dokumentowanie funkcji

def oblicz_pole_prostokata(dlugosc, szerokosc):
    """
    funcja oblicza pole prostokata
    :param dlugosc: dluzszy bok w [m]
    :param szerokosc: krotszy bok w [m]
    :return: pole prostokata w [m2]
    """
    pole = dlugosc * szerokosc
    return f'pole prostokata jest rowne: {pole}'


pole_1 = oblicz_pole_prostokata(5.0, 6.0)
pole_2 = oblicz_pole_prostokata(100,1.0)
print(pole_1)
print(pole_2)
