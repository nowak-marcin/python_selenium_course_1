# ex1:

def my_adder(a, b):
    total = a + b
    return total


my_total = my_adder(4, 5)
print(my_total)
my_total = my_adder(0, 0)
print(my_total)


# ex2:

states_with_no_sale_tax = ['AK', 'DE', 'MT', 'NH', 'OR']


def has_no_sales_tax(state):

    if state.upper() in states_with_no_sale_tax:
        return True
    else:
        return False


user_state = 'CA'
user_tax = has_no_sales_tax(user_state)
print(user_tax)

user_state = 'MT'
user_tax = has_no_sales_tax(user_state)
print(user_tax)

user_tax = has_no_sales_tax('DE')
print(user_tax)