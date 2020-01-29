#12. Utworzyc skrypt z interfejsem tekstowym obliczajacy n-ty element ciagu Fibonacciego
# - wykonac zadanie iteracyjnie i rekurencyjnie
print("program do obliczania n-tego wyrazu ciagu fibbonaciego")
def Fibonacci(n): 
    if n<0: 
        print("Zla wartosc")     
    elif n==1: 
        return 0 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
print("podaj n-ty element ciagu fibbonaciego: ")  
print(int(input())) 