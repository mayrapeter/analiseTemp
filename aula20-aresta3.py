import matplotlib.pyplot as plt
import numpy as np
import math
import pprint

k = 230
flag = False
c = 897
dens = 2700
alpha = k/(dens*c)
comprimento = 0.6
delta_c = 0.1
delta_t = 0.25*(delta_c**2)/alpha
#delta_t = 1
print("O DELTA T CERTO É",delta_t)
tempo = 7000
tamanho = 7
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
    matriz[i, tamanho-1] = 50
    #para a da esquerda 
    matriz[i, 0] = 10
    #para a de baixo 
    #matriz[tamanho-1, i] = 50


const = alpha*delta_t/(delta_c**2)

#matriz[tamanho-1, tamanho-1] = 0
matriz_temp = np.copy(matriz)


for temp in tempos:
    if (not flag):
        flag = True
        for i in range(1, tamanho):
            for j in range (1, tamanho-1):
                if i == tamanho-1:
                    matriz_temp[i,j] = const*(matriz[i,j-1] + 2*matriz[i-1,j] + matriz[i, j+1]) + matriz[i,j]*(1 - 4*const)
                else:
                    matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                erro[i,j] = abs((matriz_temp[i,j]-matriz[i,j])/matriz_temp[i,j])
                if erro[i,j] > 1e-8:
                    flag = False
        matriz = np.copy(matriz_temp)
    else:
        break


lista = []
for i in range(0, tamanho):
    lista.append(matriz[tamanho-1,i])
np.set_printoptions(precision=3)
print(matriz)
print("O tempo necessario foi", temp)
plt.matshow(matriz_temp)
plt.colorbar()
plt.show()