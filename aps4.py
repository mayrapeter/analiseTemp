#definindo
import math 
import numpy as np
import matplotlib.pyplot as plt

flag = False
alpha = 0
u = alpha
K = 1
delta_c = 1
delta_t = 0.2
Q_ponto = 100 
tempo_desp = 3 
tempo = 5
n = 2
#a = n/1.4
a = 3
#b = 60/(n+5)
b = 9
Lx = 30
Ly = 20
q = Q_ponto/(delta_c**2)
tempos = np.arange(0, tempo+delta_t, delta_t)
tamanho_x = int(1+Lx/delta_c)
tamanho_y = int(1+Ly/delta_c)
C = np.zeros([tamanho_y,tamanho_x])
C_temp = np.zeros([tamanho_y,tamanho_x])
x = np.arange(0, Lx+delta_c, delta_c)
y = np.arange(0, Ly+delta_c, delta_c)


for temp in tempos:
    for j in range(0, tamanho_x):
        for i in range(0, tamanho_y):
            if (i == 0):
                C_temp[0,j] = C[1, j]
            elif (i == tamanho_y-1):
                C_temp[i,j] = C[i-1, j]
            elif (j == 0):
                C_temp[i,0] = C[i, 1]
            elif (j == tamanho_x-1):
                C_temp[i,j] = C[i, j-1]
            else:
                if x[j] == a and y[i] == b and temp <= tempo_desp:
                    C_temp[i,j] = C[i,j] + q*delta_t + (delta_t/delta_c)*((K*(C[i+1,j]-4*C[i,j]+C[i-1,j]+C[i,j+1]+C[i,j-1])/delta_c) - (u*(C[i+1,j] - C[i-1,j])-alpha*math.sin(x[j]*math.pi/5)*(C[i,j+1]-C[i,j-1])/2))
                else:
                    C_temp[i,j] = C[i,j] + (delta_t/delta_c)*((K*(C[i+1,j]-4*C[i,j]+C[i-1,j]+C[i,j+1]+C[i,j-1])/delta_c) - (u*(C[i+1,j] - C[i-1,j])-alpha*math.sin(x[j]*math.pi/5)*(C[i,j+1]-C[i,j-1])/2))
            if C_temp[i,j] < 0:
                C_temp[i,j] = 0
    C = np.copy(C_temp)

plt.matshow(C)
plt.colorbar()
plt.show()