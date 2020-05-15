import matplotlib.pyplot as plt
import numpy as np
import math

alpha = 0.25
flag = False
comprimento = 0.5
delta_c = 0.1
delta_t = 1e-2
tempo = 1

tempos = np.arange(0, tempo+delta_t, delta_t)
erro = np.zeros([6,6])
matriz = np.zeros([6,6])
for i in range (0, 6):
    matriz[0, i] = 100

const = alpha*delta_t/(delta_c**2)

matriz_temp = np.copy(matriz)

for temp in tempos:
    if (not flag):
        for i in range(1, 5):
            for j in range (1, 5):
                matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                erro[i,j] = abs((matriz_temp[i,j]-matriz[i,j])/matriz_temp[i,j])
                if erro[i,j] <= 1e-4:
                    flag = True
    else:
        break

    matriz = np.copy(matriz_temp)
    
print("O tempo necessario foi", temp)
plt.matshow(matriz)
plt.colorbar()
plt.show()