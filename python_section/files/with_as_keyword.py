with open('demofile.txt', 'w') as my_file:
    my_file.write('pogon szczecin' + '\n')

with open('demofile.txt', 'a') as my_file:
    my_file.write('flota swinoujscie' + '\n')

with open('demofile.txt', 'r') as my_file:
    print(my_file.read())
