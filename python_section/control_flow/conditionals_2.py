theater_name = 'Kino Janusz w Szczecinie'
age_limit = 18

print(f'Witamy w: {theater_name} !!!')

user_input = int(input('Podaj swój wiek: '))
print(f'Wiek użytkownika to: {user_input} lat.')

if user_input >= age_limit:
    print('mozesz obejrzec ten film')
else:
    adult_present = input("czy jest z toba osoba dorosla? tak/nie: ")
    if adult_present.lower() == 'tak':
        print('mozesz obejrzec ten film')
    else:
        print('musisz miec ukonczone 18 lat!')
