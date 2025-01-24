# Istnieje sposób na zdefiniowanie funkcji z nieograniczoną liczbą argumentów obowiązkowych,
# przy czym nie możemy ich użyć w połączeniu z argumentami domyślnymi.

def suma_n(*args):
    return sum(args)


suma_1 = suma_n(0, 5, 10)
suma_2 = suma_n(10, 100)

print(suma_1)
print(suma_2)


# Argumenty nazwane, przekazywane w postaci słownika za pomocą **kwargs,
# pozwalają na elastyczne i czytelne wywoływanie funkcji, szczególnie gdy,
# mamy do czynienia z dużą liczbą opcjonalnych parametrów.

def zbuduj_adres(**kwargs):
    adres = ""
    if "ulica" in kwargs:
        adres += kwargs["ulica"] + ", "
    if "miasto" in kwargs:
        adres += kwargs["miasto"] + ", "
    if "kod_pocztowy" in kwargs:
        adres += kwargs["kod_pocztowy"] + ", "
    if "kraj" in kwargs:
        adres += kwargs["kraj"]
    return adres


# Przykład wywołania z pełnym zestawem argumentów
adres1 = zbuduj_adres(ulica="Kwiatowa 15", miasto="Szczecin", kod_pocztowy="71-001", kraj="Polska")
print(adres1)

# Przykład wywołania z brakującym argumentem "ulica" i "kod_pocztowy"
adres2 = zbuduj_adres(miasto="Szczecin", kraj="Polska")
print(adres2)
