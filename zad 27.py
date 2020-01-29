#27. Utwórz funkcje, która jako argument bedzie przyjmowac liste liczb zmiennoprzecinkowych,
# a jej wynikiem bedzie czwarty moment centralny (kurtoza)
from collections import Counter
import math

def srednia(x):
    return sum(x)/len(x)
    
def kurtoza(list):
    value = 0
    for x in list:
        value = (x-srednia(list))**4
    return (value / len(list)) - 3
