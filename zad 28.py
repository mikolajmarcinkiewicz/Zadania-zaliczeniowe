#28. Utwórz funkcje, która jako argument bedzie przyjmowac dwie listy o równej liczbie elementów, a jej wynikiem bedzie wspólczynnik korelacji

from collections import Counter
import math

def korelacja(listaX,listaY):
    sumaXY = 0
    for i in range(len(listaX)):
        sumaXY += listaX[i] * listaY[i]