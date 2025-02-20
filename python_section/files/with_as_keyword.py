with open('demofile.txt', 'w') as my_file:
    my_file.write('this is first line!!!')

with open('demofile.txt', 'r') as my_file:
    print(my_file.read())
