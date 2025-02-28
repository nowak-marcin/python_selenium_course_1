# ex.1:
def generate_numbers(start, end):
    my_number = start
    while my_number < end:
        yield my_number
        my_number += 1


my_generator = generate_numbers(5,11)

for my_number in my_generator:
    print(my_number)

# ex.2:
# my_generator_0_5 = (x for x in range(0,6))

