#14. Utworzyc skrypt z interfejsem tekstowym, który bedzie zwracac wiersz n-tego rzedu z trójkata Pascala (użytkownik podaje n, program zwraca odpowiadajacy wiersz trójkata)
print("to jest program do obliczania n-tego wiersza trojkanta pascala")

def pascalline(n):
     n -= 1
     line = [1]
     for k in range(max(n,0)):             
         line.append(line[k]*(n-k)//(k+1))             
     return line

print("podaj n-ty wiersz trojkanta pascala: ")
wiersz = int(input())
print(pascalline(wiersz))