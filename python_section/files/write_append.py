# r - read, w - write, a - dodaj, r+ - read and write

# utworzenie pliku, dodanie tesktu, zapis:
# jesli chcemy inny katalog to: 'C:\\Users\\nowak\\Desktop\\qa_auto_learn\\...\\writedemo.txt'

my_file = open('writedemo.txt', 'w')
my_file.write('this is first line' + '\n')
my_file.close()

# dodanie tekstu do juz utworzonego pliku (musi być typu str):

my_file = open('writedemo.txt', 'a')
l = [100, 'test', 'email', 0.25, 'janusz']
for x in l:
    my_file.write(str(x) + '\n')
my_file.close()

# odczytanie danych z pliku:

my_file = open('writedemo.txt', 'r')
print(my_file.read())
# print(my_file.readline()) - odczyta tylko piersza linie
my_file.close()