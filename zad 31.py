#31. Korzystajac z instrukcji np.random.choice
# oraz reshape z pakietu numpy stworzyc funkcje
# generuja macierz kwadratowa stopnia N wypelniona wartosciami 0 i 255 w losowy sposób


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def randomGrid(N):
    return np.random.choice([255, 0], N*N, p=[0.5, 0.5]).reshape(N, N)

print(randomGrid(10))