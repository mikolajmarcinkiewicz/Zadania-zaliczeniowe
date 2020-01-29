#13. Utworzyc skrypt z interfejsem tekstowym obliczajacy symbol Newtona n po k.
# Utworzyc funkcje, która bedzie wywolywac inna funkcje


def silnia(liczba):
    i=0
    suma=1
    while(liczba!=i):
        i += 1
        suma = suma * i
    return suma

def symbol_newtona(n,k):
    mianownik = silnia(k)*silnia(n-k)
    wynik = silnia(n) / mianownik
    return print(wynik)

print("Program do obliczania symbolu newtona")

print("Podaj wartoć n ")
number1 = int(input()) 
print("podaj wartoć k")
number2 = int(input()) 


symbol_newtona(number1,number2)