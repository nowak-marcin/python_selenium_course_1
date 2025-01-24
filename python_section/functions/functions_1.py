#   def my_first_function(parameters)
#       <code here>
#       return <something>

# Słowo kluczowe return powoduje opuszczenie funkcji (instrukcje umieszczone poniżej nie są wykonywane).
# Return pozwala również na przekazanie wartości z wnętrza funkcji do reszty programu
# parameters i return - sa opcjonalne
# zmienne w funkcji sa uzyte tylko lokalnie - w funkcji i jej wywolaniu
# jesli chcemy uzyc globalnie - global
# parametres - moga miec zdefiniowane wartosci domyslne (keyword params)


def my_adding_func(a, b=1):
    return a + b


def my_multi_func(a, b):
    if a != 0 and b != 0:
        multi = a * b
        return f'iloczyn liczb wynosi {multi}'
    else:
        return 'jedna z liczb to zero!'


value1 = my_adding_func(5, 10)
print(value1)
value2 = my_adding_func(5)
print(value2)
value3 = my_multi_func(3,5)
print(value3)
value4 = my_multi_func(0,2)
print(value4)


# dokumentowanie funkcji

def oblicz_pole_prostokata(dlugosc, szerokosc):
    """
    Funkcja oblicza pole prostokata.
    :param dlugosc: float, w metrach
    :param szerokosc: float, w metrach
    :return: pole, w metrach kwadratowych
    """
    return dlugosc * szerokosc


pole_1 = oblicz_pole_prostokata(5.0, 6.0)
pole_2 = oblicz_pole_prostokata(100,1.0)

print(pole_1)
print(pole_2)
