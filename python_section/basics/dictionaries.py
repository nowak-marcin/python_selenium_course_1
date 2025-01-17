# nieindeksowany
# można modyfikować
# klucz niepowtarzalny
# {key:value}

capitals = {'usa': 'washington', 'france': 'paris', 'turkey': 'ankara'}

print(type(capitals))

france_capital = capitals['france']
print(france_capital)

france_capital2 = capitals.get('france')
print(france_capital2)

ethiopia_capital = capitals.get('ethiopia')
print(ethiopia_capital)

ethiopia_capital2 = capitals.get('ethiopia', 'brak takiej stolicy')
print(ethiopia_capital2)

# dodawanie danych #1

capitals['kenya'] = 'nairobi'
print(capitals)

# dodawanie danych #2

capitals.update({'india': 'new dehli'})
print(capitals)

print('==========')

all_keys = capitals.keys()
all_values = capitals.values()
print(all_keys)
print(all_values)

# inny przykład słownika z listą

foot_player = {'name': 'tsubasa ozora',
                'age': 35,
                'country': 'japan',
                'clubs': ['nankatsu', 'jeziorak', 'pogon']
              }

foot_player_clubs = foot_player['clubs']
print(foot_player_clubs)