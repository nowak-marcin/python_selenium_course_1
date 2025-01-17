shows = ['Captain Tsubasa', 'Married with Children', 'Sailor Moon', 'Trailer Park Boys']
movies = ['Rocky', 'Rambo', 'Uciekinier', 'Terminator']
on_demand = ['Mis Pushupek']

my_choice = input('Podaj tytuł: ')

if (my_choice in shows) or (my_choice in movies):
    print('twoj tytul dostepny jest w serialach lub filmach')
elif my_choice in on_demand:
    print('musisz zamowic ten serial/film')
else:
    print('brak takiej pozycji')

print('=======================')

theater_name = 'Teatr Polski w Szczecinie'
age_limit = 18

print(f'Witamy w: {theater_name} !!!')

user_input = int(input('Podaj swój wiek: '))
print(f'Wiek użytkownika to: {user_input} lat.')

if user_input >= age_limit:
    print('mozesz obejrzec ten film')
else:
    print('musisz miec ukonczone 18 lat!')
