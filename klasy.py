from faker import Faker
fake = Faker()

class wizytowka:
    def __init__(self,imie, nazwisko,telefon,email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

#tworzenie list poszczególnych danych
lista_imie = []
lista_nazwisko = []
lista_telefon = []
lista_email = []

#petla generujace losowe dane
for x in range(5):
    lista_imie.append(fake.first_name())
    lista_nazwisko.append(fake.last_name())
    lista_telefon.append(fake.phone_number())
    lista_email.append(fake.ascii_email())

#tworzenie listy osob
lista_osob = []

#tworzenie pelnych wizytowek, poszczeoglne miejsca listy do kolejne wizytowki
for y in range(5):
    lista_osob.append((lista_imie[y],lista_nazwisko[y],lista_telefon[y],lista_email[y]))

#a,b,c,d,e - sa to kolejne wizytowki z uporzadkowaniem wg klasy "wizytowka"
a = wizytowka(lista_imie[0],lista_nazwisko[0],lista_telefon[0],lista_email[0])
b = wizytowka(lista_imie[1],lista_nazwisko[1],lista_telefon[1],lista_email[1])
c = wizytowka(lista_imie[2],lista_nazwisko[2],lista_telefon[2],lista_email[2])
d = wizytowka(lista_imie[3],lista_nazwisko[3],lista_telefon[3],lista_email[3])
e = wizytowka(lista_imie[4],lista_nazwisko[4],lista_telefon[4],lista_email[4])

#dziedziczenie klasy wizytowka
class BusinessContact(wizytowka):
   def __init__(self, stanowisko, firma, telefon_sluzbowy, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.stanowisko = stanowisko
       self.firma = firma
       self.telefon_sluzbowy = telefon_sluzbowy

lista_stanowisko = []
lista_firma = []
lista_sluzbowy = []

for x in range(5):
    lista_stanowisko.append(fake.job())
    lista_firma.append(fake.company())
    lista_sluzbowy.append(fake.phone_number())

lista_wizytowek_sluzbowych = []
    
for z in range(5):
    lista_wizytowek_sluzbowych.append((lista_imie[z],lista_nazwisko[z],lista_telefon[z],lista_email[z],lista_stanowisko[z],lista_firma[z],lista_sluzbowy[z]))

a_sluzbowy = BusinessContact(imie = lista_imie[0], nazwisko = lista_nazwisko[0],telefon = lista_telefon[0], email = lista_email[0], stanowisko = lista_stanowisko[0], firma = lista_firma[0], telefon_sluzbowy = lista_sluzbowy[0])
b_sluzbowy = BusinessContact(imie = lista_imie[1], nazwisko = lista_nazwisko[1],telefon = lista_telefon[1], email = lista_email[1], stanowisko = lista_stanowisko[1], firma = lista_firma[1], telefon_sluzbowy = lista_sluzbowy[1])
c_sluzbowy = BusinessContact(imie = lista_imie[2], nazwisko = lista_nazwisko[2],telefon = lista_telefon[2], email = lista_email[2], stanowisko = lista_stanowisko[2], firma = lista_firma[2], telefon_sluzbowy = lista_sluzbowy[2])
d_sluzbowy = BusinessContact(imie = lista_imie[3], nazwisko = lista_nazwisko[3],telefon = lista_telefon[3], email = lista_email[3], stanowisko = lista_stanowisko[3], firma = lista_firma[3], telefon_sluzbowy = lista_sluzbowy[3])
e_sluzbowy = BusinessContact(imie = lista_imie[4], nazwisko = lista_nazwisko[4],telefon = lista_telefon[4], email = lista_email[4], stanowisko = lista_stanowisko[4], firma = lista_firma[4], telefon_sluzbowy = lista_sluzbowy[4])

dane_wprowadzajace = int(input("Wybierz rodzaj wizytowki (biznesowa (1) lub podstawowa (2) ): "))
wybor_wizytowki = int(input("Wybierz wizytowke (0,1,2,3,4): "))


if dane_wprowadzajace == 1:
    wynik = f"Wybieram numer {lista_sluzbowy[wybor_wizytowki]} i dzwonie do {lista_imie[wybor_wizytowki]} {lista_nazwisko[wybor_wizytowki]}"
    print(wynik)
    print(f"Dlugosc imienia i nazwiska to: {len(lista_imie[wybor_wizytowki])+len(lista_nazwisko[wybor_wizytowki])}")
if dane_wprowadzajace == 2:
    wynik2 = lista_imie[wybor_wizytowki]
    print(wynik2)
    print(f"Dlugosc imienia i nazwiska to: {len(lista_imie[wybor_wizytowki])+len(lista_nazwisko[wybor_wizytowki])}")
    