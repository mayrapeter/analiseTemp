import matplotlib.pyplot as plt
import numpy as np
import math

k = 230
c = 897
dens = 2.7 * 1e3
alpha = k/(dens*c)
flag = False
comprimento = 0.4
delta_c = 0.01
delta_t = 0.25*(delta_c**2)/alpha
print("O DELTA T É, ", delta_t)
tempo = 10000

tempos = np.arange(0, tempo+delta_t, delta_t)
tamanho = 41
erro = np.zeros([tamanho,tamanho])
matriz = np.zeros([tamanho,tamanho])
for i in range (0, tamanho):
    #para a de cima
    matriz[0, i] = 100
    #para a da direito 
    matriz[i, tamanho-1] = 50
    #para a da esquerda 
    matriz[i, 0] = 75
    #para a de baixo 
    #matriz[tamanho-1, i] = 150

const = alpha*delta_t/(delta_c**2)

matriz_temp = np.copy(matriz)

for temp in tempos:
    if (not flag):
        flag = True
        for i in range(1, tamanho-1):
            for j in range (1, tamanho-1):
                matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                erro[i,j] = abs((matriz_temp[i,j]-matriz[i,j])/matriz_temp[i,j])
                if erro[i,j] > 1e-8:
                    flag = False
    else:
        break

    matriz = np.copy(matriz_temp)
maior_erro = 0
for i in range(1, tamanho-1):
    for j in range (1, tamanho-1):
        if erro[i,j] > maior_erro:
            maior_erro = erro[i,j]
print("O MAIOR ERRO E", maior_erro)
print(matriz)
print("O elemento e",matriz[20,20])
print("O tempo necessario foi", temp)
plt.matshow(matriz)
plt.colorbar()
plt.show()