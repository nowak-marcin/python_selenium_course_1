first_number = int(input('podaj piersza liczbe: '))
second_number = int(input('podaj druga liczbe: '))
third_number = int(input('podaj trzecia liczbe: '))

print(f'twoje liczby to {first_number} - {second_number} - {third_number}')

if first_number == second_number == third_number:
    print('podales trzy takie same liczby')
else:
    print('podales przynajmniej dwie rozne liczby')

if (first_number) % 2 == 0 and (second_number) % 2 == 0 and (third_number) % 2 == 0:
    print('wszystkie liczby sa parzyste')
else:
    print('jedna lub wiecej liczb jest nieparzysta')