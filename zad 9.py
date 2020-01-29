#9. Utwórz skrypt z interfejsem tekstowym, który wyliczy sume n kolejnych liczb (użytkownik podaje pierwsza i ostatnia liczbe sumy).
# Uwaga - w zadaniu należy zbudowac funkcje wlasna realizujaca dane zadanie
print("Program do znajdywania sumy n liczb")
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)
print("Podaj n: ")   
num = int(input())

if num < 0:
   print("Podaj dodatnia wartosc")
else:
   print("Suma wynosi",recur_sum(num))