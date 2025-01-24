class Osoba:
    # konstruktor klasy:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    # metoda klasy:
    def przedstaw_sie(self):
        print(f'Czesc, jestem {self.imie} {self.nazwisko}')


# tworzenie obiektów (instancji) klasy Osoba:
osoba1 = Osoba('jan', 'kowalski')
osoba2 = Osoba('karol', 'malinowski')

# wywołanie metody klasy dla obiektów:
osoba1.przedstaw_sie()
osoba2.przedstaw_sie()
