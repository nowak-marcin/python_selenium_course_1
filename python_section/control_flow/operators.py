# Boolean: True, False
# operatory: arithmetic, comparison, logical

liczba1 = int(input('podaj pierszą liczbę (1-9): '))
liczba2 = int(input('podaj drugą liczbę (1-9): '))

wynik = liczba1 + liczba2
print(f'suma liczb wynosi {wynik}')

if liczba1 > liczba2:
    print('pierwsza liczba jest większa od drugiej')
elif liczba1 < 1 or liczba2 < 1:
    print('jedna z liczb jest mniejsza od 1')
elif liczba1 > 9 or liczba2 > 9:
    print('jedna z liczb jest większa od 9')
elif liczba1 == liczba2:
    print('liczby są sobie równe')
else:
    print('druga liczba jest większa od pierwszej')