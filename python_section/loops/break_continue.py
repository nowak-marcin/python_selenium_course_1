# Instrukcja break kończy działanie bieżącej pętli i
# przenosi wykonanie do kodu umieszczonego bezpośrednio po niej
# Instrukcja continue pomija pozostałą część bieżącej iteracji pętli
# i przechodzi bezpośrednio do kolejnej iteracji. Może być używana,
# jeśli chcemy pominąć pewne instrukcje w bieżącej iteracji na podstawie pewnego warunku.
# Zamiast więc przerywać całe działanie pętli, przechodzimy do następnego obiegu.


for i in range(10):
    if i == 5:
        break
    print(i)

print('======')

for i in range(10):
    if i % 2 == 0:  # jeśli i jest liczbą parzystą
        continue
    print(i)

print('======')

main_number = 15
my_input = 0
while True:
    my_input = int(input('podaj liczbe od 0 do 20: '))
    print(f'podales liczbe: {my_input}')
    if my_input == main_number:
        break
print('done!!!')

print('======')

capitals = {
    'peru': 'lima',
    'philippines': 'manila',
    'spain': 'madrit',
    'ethiopia': 'addis ababa',
    'ghana': 'accra'
}

my_input = input('podaj kraj: ')
for country, capital in capitals.items():
    print('podany kraj to:', country)
    if my_input.lower() == country.lower():
        print('stolica jest:', capital)
        break

print('======')

book_prices = {'calculus': 300, 'physics': 255, 'chemistry': 400, 'english': 150, 'theather': 100}
my_courses = {'physics', 'english', 'psychology', 'calculus', 'history'}

total_cost = 0
for course in my_courses:
    if course not in book_prices.keys():
        continue
    total_cost += book_prices[course]
    total_cost = total_cost + book_prices[course]
print(f'calkowita cena podrecznikow do kursu wynosi {total_cost}')