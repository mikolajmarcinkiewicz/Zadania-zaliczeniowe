#4. Utwórz skrypt do znajdowania miejsc zerowych trójmianu kwadratowego x1 = (-b+sqrt(b*b-4*a*c))/(2*a)
#x2 = (-b-sqrt(b*b-4*a*c))/(2*a)

print("Program do znajdwyania miejsc zerowych trójmianu kwadratowego")
print("Podaj a trojmianu:")
a = int(input())
print("Podaj b trojmianu:")
b = int(input())
print("Podaj c trojmianu:")
c = int(input())

if b*b-4*a*c > 0:
    print("x1 = :")
    print((-b+(b*b-4*a*c)**(1/2))/(2*a))
    print("x2 = :")
    print((-b-(b*b-4*a*c)**(1/2))/(2*a))
if b*b-4*a*c == 0:
    print("x0 = ")
    print((-b/(2*a)))
if b*b-4*a*c < 0:
    print("miejsca zerowe nie istnieje w zbiorze liczb rzeczywistych")