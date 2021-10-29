# 2


zmienna1 = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

imie = "Patryk"
nazwisko = "Sulewski"

liczba_liter2 = zmienna1.count(nazwisko[3])
liczba_liter1 = zmienna1.count(imie[2])

print("w tekście jest", liczba_liter1, "liter oraz", liczba_liter2, "liter")
# 4


zmienna_typu_string = 'Paryk Sulewski'

print(dir(zmienna_typu_string))
help(zmienna_typu_string.count('a'))
# 5
print(imie[::-1], nazwisko[::-1])

# 6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = lista[5:10:1]
del lista[5:10]
print(lista, lista2)
# 7
lista = lista + lista2
lista.insert(0, 0)
print(lista)
kopialisty = lista.copy()
kopialisty.sort()
kopialisty.reverse()
print(kopialisty)
# 8
krotka = (("Patryk Sulewski", 154418), ("Janek Spawalski", 159999), ("Mariusz Mocarski", 158999))

# 9
dct = dict((x, y) for x, y in krotka)
print(dct)
dct2 = {'Wiek': 22, 'Adres email': 'a@b.pl', 'Rok Urodzenia': 1998, 'Adres': "Mykicin 17"}
dct3 = {'Wiek': 23, 'Adres email': 'a@d.pl', 'Rok Urodzenia': 1997, 'Adres': "Mykicin 16"}
dct4 = {'Wiek': 29, 'Adres email': 'a@c.pl', 'Rok Urodzenia': 1995, 'Adres': "Mykicin 15"}
print(dct2)
print(dct3)
print(dct4)
# 10
numlista = [560445999, 243345666, 222333444, 555444333, 777666888, 555444777, 565445567, 333666888, 999666555,
            333444555, 222333444, 777666888, 444999777, 666999111, 222333444, 111888444, 555111999, 555888444,
            222333111, 555999444, 222444777, 444333666, 555666111, 333666999, 222444222, 111111111, 222222222,
            333333333, 444444444, 555555555, 666666666, 777777777, 888888888, 999999999]

for f in set(numlista):
    print(f)

# 11
numlista.sort()
print('Lista rosnąco 10')
for i in range(1, 11):
    print(numlista[i])

# 12
print("Lista malejąco")
num2lista = numlista.copy()
set(num2lista)
num2lista.sort()
num2lista.reverse()

print(num2lista[100:20:-5])
# 13

listosłownik = [{'klucz1': 222, 'klucz2': 333, 'klucz3': 'aaa'}, {'klucz4': 333, 'klucz5': 666, 'klucz6': 'bbb'}]


def wypisz(lista):
    string = ''
