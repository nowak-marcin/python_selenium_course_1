# zasiegi zmiennych:
# local - definicja zmiennej znajduje się wewnatrz danej funkcji lub klasy, niedostepne na zewnatrz
# enclosing - definicja zmiennej funcji a jest znajduje sie wewnatrz zagniezdzonej funkcji b
# global - zasieg na poziomie skryptu / pliku
# bulit-in - zmienne wbudowane, ogolnodostepne


salary1 = int(input('podaj pensje 1: '))
salary2 = int(input('podaj pensje 2: '))
euro = 3.99

def add_my_salary_1(c=0.20):
    extra = (salary1 + salary2) * c
    return salary1 + salary2 + extra

def add_my_salary_2(d=0.30):
    extra = (salary1 + salary2) * d
    return salary1 + salary2 + extra

def salary_in_euro():
    return (salary1 + salary2) / euro


value1 = add_my_salary_1()
print(value1)
value2 = add_my_salary_2(0.40)
print(value2)
value3 = salary_in_euro()
print(value3)
