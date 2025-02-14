# string-metods (str):

wage = '7000'
employee = 'ZS-5 pracownik 1'

print(employee[3], employee[-1], employee[0:4])
print(len(employee))

print('==========')

e = ' Hello World!'

print(e.upper(), e.lower())
print(e.strip())
print(e.count('l'))
print(e.split())
print(e.endswith('!'), e.startswith(' '))
print(e.replace(' ', '%'))
print(e[1:12])

print('=========')
# string formatting:

player_name = input('Podaj dane piłkarza: ')
age = int(input('Podaj wiek: '))

print(f'Wybrany piłkarz to {player_name} i ma {age} lat.')
print('Wybrany piłkarz to:', player_name, 'i ma lat:', age)

print('=========')
# string join:

main_page = 'www.24kurier.pl'
party_cart = '/imprezy'

party_page = main_page + party_cart
print(party_page)

data_list = ['71-699', 'Szczecin', 'ZPM']
print(', '.join(data_list))
