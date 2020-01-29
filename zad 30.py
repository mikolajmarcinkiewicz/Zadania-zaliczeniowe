#30. Wynegeruj liste 1000 liczb losowych o rozkladzie normalnym.
# Wykresl histogram oraz srednia, mediane, dominante,
# odchylenie standardowe, wariancje, skosnosc i kurtoze
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import math
def srednia(x):
    return sum/len(x)

def dominanta(z):
    c = Counter(list)
    return c.most_common(1)[0][0]
            
def od_sta_sre(list):
    value = 0 
    for x in list:
        value = (x- srednia(list))**2
    return math.sqrt(value / len(list))
    
def wariacja(list):
    value = 0
    for x in list:
            value = (x-srednia(list))**2
    return (value/ len(list))
            
def skosnosc(list):
    value = 0
    for x in list:
            value = (x-srednia(list))**3
    return (value/ len(list))
    
def kurtoza(list):
    value = 0
    for x in list:
        value = (x-srednia(list))**4
    return (value / len(list)) - 3
   
lista = []    
for i in (0,1000):
    lista.append(np.random.normal(0,1000))
    
while len(lista) < 1000:
    lista.append(np.random.normal(0,1000))
    
plt.hist(lista, 30, density=True)
print("srednia wynosi: ",srednia(lista))
print("mediana wynosi: ",np.mean(lista))
print("dominanta wynosi: ",dominanta(lista))
print("odchylenie standardowe wynosi: ",od_sta_sre(lista))
print("wariacja wynosi: ",wariacja(lista))
print("skosnosc wynosi: ",skosnosc(lista))
print("kurtoza wynosi: ",kurtoza(lista))

