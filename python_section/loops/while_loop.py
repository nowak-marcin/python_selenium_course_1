# ctrl+c - przerywa petle nieskonczona
# while - petla wykonuje sie dopoki warunek zmieni się z true na false

counter = 0
while counter < 4:
    print(f'obecny numer to: {counter}')
    counter += 1


main_number = 8
my_input = 0
while my_input != main_number:
    my_input = int(input('podaj liczbe od 0 do 10: '))
    print(f'podales liczbe: {my_input}')
    print(my_input != main_number)
print('done!!!')
