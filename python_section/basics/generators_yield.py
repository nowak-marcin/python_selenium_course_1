# ex.1:
def generate_numbers(start, end):
    number = start
    while number < end:
        yield number
        number += 1

my_generator = generate_numbers(5,11)

for number in my_generator:
    print(number)

print('------------')

#ex.2:
def get_doubles(my_list:list):
    for element in my_list:
        yield element * 2

numbers = get_doubles([2,4,6])
print(next(numbers))
print(next(numbers))
print(next(numbers))

print('------------')

# ex.3:
for x in (x for x in range(0,6)):
    print(x)

print('------------')

# ex.4:
my_list = [3,5,7]

for x in (x*2 for x in my_list):
    print(x)

print('------------')
