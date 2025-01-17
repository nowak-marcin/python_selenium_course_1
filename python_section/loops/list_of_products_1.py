"""
Exercise 1:
- Iterate the products list and print the name of all products that have price greater than 25.
Exercise 2:
- Print the name and price of products that are on sale.
Exercise 3:
- Create a list of products (product names) that are on sale but do not have a sale price.
"""

products = [
    {'id': 1, 'name': 't-shirt', 'price': 12.99, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': 22.45, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': 43.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': 14.99, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': 32.50, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': 150.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]

print('Exercise 1:')

for i in products:
    if i['price'] > 25:
        print(i['name'])


print('Exercise 2:')

for i in products:
#   if i['is_on_sale'] == True:
    if i['is_on_sale']:
        print(i['price'])
        print(i['name'])


print('Exercise 3:')

no_price_list = []
for i in products:
#   if i['is_on_sale'] == True and i['sale_price'] == None:
    if i['is_on_sale'] and not i['sale_price']:
        no_price_list.append(i['name'])
print(no_price_list)


# Ex1 dla ceny jako string np. 'price': '$150'

# for i in products:
#   tmp_price = i['price'][1:] - I sposob
#   tmp_price = i['price'].replace('$', '') - II sposob
#   price = float(tmp_price)
#   if price > 25:
#       print(i['name'])