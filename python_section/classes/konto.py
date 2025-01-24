# private metod (__) - dostepna tylko z wywolanie tej danej klasy, nie z zewnatrz
# (w python to fikcja)
# ostatniej __metody read_balance_from_database nie mozna wywolac z zewnatrz


import random

class Account(object):
    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f'Obecny balance dla tego usera wynosi: {self.current_balance} {self.currency}')

    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f'Nowy balance dla {self.user_id} po wyplacie wynosi: {self.current_balance} {self.currency}')

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f'Nowy balance dla {self.user_id} po wplacie wynosi: {self.current_balance} {self.currency}')

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):
        print(f'Pobierz balance z bazy dla usera: {self.user_id}')
        return random.randint(100, 200)


account1 = Account(17256)
account2 = Account(20222, currency='PLN')
print('=============')
account1.deposit(100)
account2.withdraw(100)
