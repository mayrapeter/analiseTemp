import matplotlib.pyplot as plt
import numpy as np

alpha = 1
comprimento = 50
delta_t = 5
T_inicial = 0
T_atual = 20
T_comprimento = 0

Temp = [0,T_atual, T_atual, T_atual, T_atual, T_atual, T_atual, T_atual, T_atual, T_atual, 0]
X = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]

temp3 = [0,0,0,0,0,0,0,0,0,0,0]

for z in range(0, 540, 5):
    j = 1
    for i in range(5, comprimento, 5):
        X[j] = i
        temp3[j] = Temp[j] + (1/5)*(Temp[j-1] - 2*Temp[j] + Temp[j+1])
        j += 1

    Temp = np.copy(temp3)

print(temp3)
print(len(Temp))
print(X)
print(len(X))

plt.plot(X, Temp)
plt.xlabel('Posição(m)')
plt.ylabel('Temperatura(K)')
plt.title('Gráfico temperatura x posição')
plt.show()