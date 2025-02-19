# dodanie breakpoint w kodzie:
#   import pdb
#   ...
#   pdb.set_trace()

# konsola (pdb):
# c - continue, n - stop after executing next line, s - stop as soon as possible
# l - show current line, pp - pretty print np w formacie json, h - help
# mozna podwac nazwy zmiennych np f_name

import pdb

# ex.1:

print('jestem w pierwszej linii')
f_name = 'adam'
l_name = 'kinfu'

pdb.set_trace()

print('jestem w drugiej linii')
print('jestem w trzeciej linii')
print(f'imie: {f_name}, nazwisko: {l_name}')


print('-------------')
# ex.2:

def get_user_name(name):
    user_names = {'admask': 'ak',
                  'joe': 'joe99',
                  'mary': 'maryrocks2020'}
    print(f'zalogowany uzytkownik to: {user_names[name]}')
    return user_names[name]


name = 'admask'
user_1 = get_user_name(name)

pdb.set_trace()

user_2 = get_user_name('joe')
