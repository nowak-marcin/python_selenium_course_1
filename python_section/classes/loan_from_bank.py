# Zmienne klasowe służą jako współdzielone atrybuty we wszystkich instancjach klasy,
# zapewniając scentralizowany sposób zarządzania danymi wspólnymi dla całej klasy.
# przyklad dla 'spread':


class Bank:
    spread = 0.20

    def __init__(self, customer_name, loan_amount):
        self.customer_name = customer_name
        self.loan_amount = loan_amount

    def calculate_repaid_amount(self):
        repaid_amount = (self.loan_amount * self.spread) + self.loan_amount
        print(f'Klient: {self.customer_name}')
        print(f'calkowita kwota do splaty wynosi {repaid_amount}.')

    def calculate_repaid_amount_with_penalty(self, penalty_percent):
        penalty = penalty_percent * self.loan_amount
        repaid_amount_with_penalty = (self.loan_amount * self.spread) + self.loan_amount + penalty
        print(f'Klient: {self.customer_name}')
        print(f'calkowita kwota do splaty wynosi {repaid_amount_with_penalty}.')


customer1 = Bank('janusz kowal', 1000)
customer1.calculate_repaid_amount()
customer2 = Bank('maciej koch', 1000)
customer2.calculate_repaid_amount_with_penalty(0.10)
