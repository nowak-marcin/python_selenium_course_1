# W powyższym przykładzie klasa Pracownik korzysta z kompozycji,
# umieszczając obiekt klasy Pensja jako jej atrybut.
# Dzieki temu Pracownik może korzystać z metod zdefiniowanych w klasie Pensja poprzez instancję tej klasy.

# Metoda __str__ w Pythonie pozwala nam zdefiniować niestandardową reprezentację obiektu
# w postaci ciągu znaków.
# Domyślnie, gdy drukujemy obiekt lub konwertujemy go na ciąg znaków za pomocą str()


class Pensja:
    def __init__(self, pensja: int, stopa_podwyzki: float):
        self.pensja = pensja
        self.stopa_podwyzki = stopa_podwyzki

    def roczna_pensja(self):
        return self.pensja * (1 + self.stopa_podwyzki)

    def __str__(self):
        return f'Pensja: {self.pensja}, Stopa podwyżki: {self.stopa_podwyzki*100}%'

class Pracownik:
    def __init__(self, imie: str, nazwisko: str, pensja: Pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja # kompozycja: obiekt Pensja jest częścią obiektu Pracownik

    def __str__(self):
        return f'Pracownik: {self.imie} {self.nazwisko}, Zarabia rocznie: {self.pensja} PLN'


pracownik1 = Pracownik('jan', 'kowalski', 7000)
print(pracownik1)
pracownik2 = Pensja(7000, 0.05)
print(pracownik2)
