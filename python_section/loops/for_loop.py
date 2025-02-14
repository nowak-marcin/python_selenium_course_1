my_list = ['bike', 'car', 'house', 'boat']

for i in my_list:
    print(i)
    print('-------')


my_text = 'Pociag odjezdza dzis z peronu 2 / toru 5.'

for i in my_text.split():
    if len(i) <= 3:
        print(i)
    else:
        pass

small_words = []
for i in my_text.split():
    if len(i) <= 3:
        small_words.append(i)
print(small_words)


my_list = [['india', 'delhi'], ['germany', 'berlin'], ['norway', 'oslo']]
my_dict = dict(my_list)
print(my_dict)
for country, city in my_dict.items():
    print(country, city)
