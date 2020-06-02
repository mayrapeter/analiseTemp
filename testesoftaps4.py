#definindo
import math 
import numpy as np
import matplotlib.pyplot as plt

flag = False
alpha = 0
alpha_v = 0
u = 1
K = 1
delta_c = 0.5
delta_t = 0.05
Q_ponto = 80
tempo_desp = 2
tempo = 5
a = 15
b = 15
Lx = 30
Ly = 30
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
                    C_temp[i,j] = C[i,j] + q*delta_t + (delta_t/delta_c)*((K*(C[i+1,j]-4*C[i,j]+C[i-1,j]+C[i,j+1]+C[i,j-1])/delta_c) - 0.5*u*(C[i,j+1] - C[i,j-1]) + 0.5*alpha*math.sin(x[j]*math.pi/5)*(C[i+1,j]-C[i-1,j]))
                else:
                    C_temp[i,j] = C[i,j] + (delta_t/delta_c)*((K*(C[i+1,j]-4*C[i,j]+C[i-1,j]+C[i,j+1]+C[i,j-1])/delta_c) - 0.5*u*(C[i,j+1] - C[i,j-1]) + 0.5*alpha*math.sin(x[j]*math.pi/5)*(C[i+1,j]-C[i-1,j]))
            if C_temp[i,j] < 0:
                C_temp[i,j] = 0
    C = np.copy(C_temp)
#print("O tempo esta", temp)
print("O elemento e ", C[40][40])
plt.matshow(C)
plt.colorbar()
plt.show()