import matplotlib.pyplot as plt
import numpy as np
import math

k = 2.3
c = 897
dens = 2.7 * 10e-3
alpha = k/(dens*c)
flag = False
comprimento = 0.4
delta_c = 0.1
delta_t = 10e-3
tempo = 10
tamanho = 12
# tarefa 1: O significado do termo é a variação de temperatura na borda e na mesma altura na direcao x
#digite 0 para a da esquerda, 1 para a de cima, 2 para a da direita e 3 para a de  baixo
aresta = 0
tempos = np.arange(0, tempo+delta_t, delta_t)
erro = np.zeros([tamanho,tamanho])
matriz = np.zeros([tamanho,tamanho])

for i in range (0, tamanho):
    #para a de cima
    matriz[0, i] = 150
    #para a da direito 
    matriz[i, tamanho-1] = 50
    #para a da esquerda 
    #matriz[i, 0] = 150
    #para a de baixo 
    #matriz[tamanho-1, i] = 150


const = alpha*delta_t/(delta_c**2)
print(const)
matriz_temp = np.copy(matriz)

for temp in tempos:
    if (not flag):
        flag = True
        if aresta == 0:
            for i in range(1, tamanho-1):
                for j in range (0, tamanho-1):
                    if j == 0:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    else:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    erro[i,j] = abs((matriz_temp[i,j]-matriz[i,j])/matriz_temp[i,j])
                    if erro[i,j] > 10e-8:
                        flag = False
        elif aresta == 1:
            for i in range(0, tamanho-1):
                for j in range (1, tamanho-1):
                    if i == 0:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    else:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    erro[i,j] = abs((matriz_temp[i,j]-matriz[i,j])/matriz_temp[i,j])
                    if erro[i,j] > 10e-8:
                        flag = False
        elif aresta == 2:
            for i in range(1, tamanho-1):
                for j in range (1, tamanho):
                    if j == tamanho-1:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    else:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    erro[i,j] = abs((matriz_temp[i,j]-matriz[i,j])/matriz_temp[i,j])
                    if erro[i,j] > 10e-8:
                        flag = False
        else:
            for i in range(1, tamanho):
                for j in range (1, tamanho-1):
                    if i == tamanho-1:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    else:
                        matriz_temp[i,j] = const*(matriz[i+1,j] + matriz[i-1,j] + matriz[i,j+1] + matriz[i,j-1]) + matriz[i,j]*(1 - 4*const)
                    erro[i,j] = abs((matriz_temp[i,j]-matriz[i,j])/matriz_temp[i,j])
                    if erro[i,j] > 10e-8:
                        flag = False
        matriz = np.copy(matriz_temp)
    else:
        break

lista = []
for i in range(0, tamanho):
    lista.append(matriz[i,0])
print(lista)
print("O tempo necessario foi", temp)
plt.matshow(matriz_temp)
plt.colorbar()
plt.show()