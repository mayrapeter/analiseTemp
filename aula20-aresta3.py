import matplotlib.pyplot as plt
import numpy as np
import math

k = 230
c = 897
dens = 2.7 * 1e3
alpha = k/(dens*c)
comprimento = 0.4
delta_c = 0.4/9
delta_t = 1e-3
tempo = 10
tamanho = 10
# tarefa 1: O significado do termo é a variação de temperatura na borda e na mesma altura na direcao x
#digite 0 para a da esquerda, 1 para a de cima, 2 para a da direita e 3 para a de  baixo
aresta = 1
tempos = np.arange(0, tempo+delta_t, delta_t)
erro = np.zeros([tamanho,tamanho])
matriz = np.zeros([tamanho,tamanho])

for i in range (0, tamanho):
    #para a de cima
    matriz[0, i] = 100
    #para a da direito 
    #matriz[i, tamanho-1] = 150
    #para a da esquerda 
    matriz[i, 0] = 150
    #para a de baixo 
    #matriz[tamanho-1, i] = 50


const = alpha*delta_t/(delta_c**2)

#matriz[tamanho-1, tamanho-1] = 0
matriz_temp = np.copy(matriz)


for temp in tempos:
    for i in range(1, tamanho):
        for j in range (1, tamanho-1):
            if i == tamanho-1:
                matriz_temp[i,j] = const*(matriz[i,j-1] + 2*matriz[i-1,j] + matriz[i, j+1]) + matriz[i,j]*(1 - 4*const)
            else:
                matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)

    matriz = np.copy(matriz_temp)


lista = []
for i in range(0, tamanho):
    lista.append(matriz[tamanho-1,i])
print(lista)
print("O tempo necessario foi", temp)
plt.matshow(matriz_temp)
plt.colorbar()
plt.show()