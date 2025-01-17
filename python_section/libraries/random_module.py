# wbudowane (wystarczy import) lub zewnetrzne (trzeba pobrac i zainstalowac)
# przyklady wbudowanych: datetime, random, os, urllib, pprint, ...
# przykady zewnetrznych: selenium, requests, ...

# $ pip install requests
# import requests
# page = requests.get('http://demostore.superqa.com')

# $ pip install selenium
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://demostore.superqa.com')

# oznaczanie biblioteki aliasem:
# import pymysql as db
# connection = db.connect('1.1.1.1', user='admas', password='abc123')

# ex1:

import random

any_number = random.randint(100,200)
print(any_number)

any_number = random.randrange(20)
print(any_number)


# ex2:

my_list = ['test1', 'uat3.0', 'preprod', 'user6', 'test_user_789']

a = random.choice(my_list)
print(a)
b = random.sample(my_list, 3)
print(b)

