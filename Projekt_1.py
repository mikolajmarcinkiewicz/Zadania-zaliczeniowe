#1. Utwórz program do nauki obcych slówek.
#Nie jestem wstanie dokonczyc wstwiam moj progres
import os
f1 = open("Slownik1.txt","wb")

def pobierz_dane(plikcsv):
    """
    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """
    dane = []  # deklarujemy pustą listę
    if os.path.isfile(plikcsv):  # sprawdzamy czy plik istnieje na dysku
        with open(plikcsv, "r") as zawartosc:  # otwieramy plik do odczytu
            for linia in zawartosc:
                linia = linia.replace("\n", "")  # usuwamy znaki końca linii
                linia = linia.replace("\r", "")  # usuwamy znaki końca linii
                linia = linia.encode("utf-8")  # odczytujemy znaki jako utf-8
                # dodajemy elementy do tupli a tuplę do listy
                dane.append(tuple(linia.split()))
    else:
        print( "Plik z danymi", plikcsv, "nie istnieje!")

    return tuple(dane)  # przekształcamy listę na tuplę i zwracamy ją


print("program do nauki obcych slowek")
print("podaj date nauki: ")
data = input()
f1.write("Lekcja ta odbyla sie: ".encode())
f1.write(data.encode())

slowka_do_nauki = pobierz_dane('Zeszyt1.csv')
for i in range(len(slowka_do_nauki)):
    slowka_do_nauki[i][0]
Slownik = {
    "krowa" : "cow",
    "miec" : "have",
    "byc" : "be"
}

for i in Slownik:
    print("Podaj angielski odpowiednik slowka: ",i)
    if input() in Slownik.values():
        print("Gratuluje dobrze odpowiedziales, powinienes powtorzyc to slowo za 7 dni")
        f1.write("\nSlowka ktore musisz powtorzyc za 7 dni: ".encode())
        f1.write(i.encode())
        f1.write(";".encode())
    else:
         print("Niestety twoja odpowiedz jest blendna")
         f1.write("\nSlowka ktore musisz powtorzyc za 0 dni: ".encode())
         f1.write(i.encode())
         f1.write(";".encode())
         
f1.close()


