class Czlowiek:
    def __init__(self, imie, nazwisko, zawod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.zawod = zawod

    def infobox(self):
        return f'Osoba to: {self.imie} {self.nazwisko}, zawód to: {self.zawod}'

    def rodo_info(self):
        print('podales swoje dane osobowe')

class Student(Czlowiek):
    def __init__(self, imie, nazwisko, zawod, kierunek, uczelnia):
        super().__init__(imie, nazwisko, zawod)
        self.kierunek = kierunek
        self.uczelnia = uczelnia

    def infobox(self):
        return f'{super().infobox()}, kierunek to: {self.kierunek}, uczelnia to: {self.uczelnia}'


czlowiek1 = Czlowiek('janusz', 'kowalski', 'kierowca')
print(czlowiek1.infobox())
czlowiek1.rodo_info()

student1 = Student('maciej', 'maj', 'elektryk', 'elektryka', 'ZUT')
print(student1.infobox())
student1.rodo_info()