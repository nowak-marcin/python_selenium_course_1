class Osoba:

    # konstruktor klasy:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    # metody klasy:
    def przedstaw_sie(self):
        print(f'Czesc, jestem {self.imie} {self.nazwisko}')

    def podaj_wiek(self):
        print(f'mam {self.wiek} lat.')


# tworzenie obiektów (instancji) klasy Osoba:
osoba1 = Osoba('jan', 'kowalski', 54)
osoba2 = Osoba('karol', 'malinowski', 60)

# wywolanie metody klasy dla obiektów:
osoba1.przedstaw_sie()
osoba1.podaj_wiek()
osoba2.przedstaw_sie()
osoba2.podaj_wiek()

# wywolanie parametrow metody dla obiektu:
print(osoba1.imie, osoba1.nazwisko, osoba1.wiek)
print(f'imie i nazwisko: {osoba2.imie} {osoba2.nazwisko}, wiek: {osoba2.wiek} lat')
