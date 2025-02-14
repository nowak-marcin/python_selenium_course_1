# ex1:

def get_count_of_small_word(input_string, max_size=3):

    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)

    return len(small_words)


my_text_1 = ('Puszcza Bukowa - kompleks leśny położony przy południowo-wschodnich dzielnicach Szczecina'
             ' na Wzgórzach Bukowych. Wchodzi w skład Szczecińskiego Parku Krajobrazowego Puszcza Bukowa,'
             ' utworzonego w 1981 r. oraz Leśnego Kompleksu Promocyjnego Puszcze Szczecińskie,'
             ' utworzonego w 1996 r.')

num_small = get_count_of_small_word(my_text_1)
print(num_small)
num_small = get_count_of_small_word(my_text_1, max_size=5)
print(num_small)

print('===========')
# ex2:

def connect_to_database(host='test.db.com', username='testuser', password='testpass'):
    print(f'nawiazano polaczenie z: {host}')
    print(f'dla uzytkownika: {username}')


connect_to_database()
connect_to_database('prod.db.com', 'uatuser')

print('===========')
# ex.3:

def zip_my_2_lists(my_clubs, my_cities):
    # zwroci zlaczona nazwe:
    for club, city in zip(my_clubs, my_cities):
        print(club, city)
    # zwroci slownik:
    new_zip_list = zip(my_clubs, my_cities)
    print(dict(new_zip_list))

my_clubs = ('arsenal', 'real', 'borussia', 'psg')
my_cities = ('london', 'madrit', 'dortmund', 'paris')

zip_my_2_lists(my_clubs, my_cities)