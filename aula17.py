import math
import matplotlib.pyplot as plt
L = 0.3
k = 200
l = 0.03
P = 4*l
Tb = 350
Tamb = 300
h = 15
A = l*l

temp = []
xs = []
m = math.sqrt(h*P/(k*A))
x = 0
while (x < L):
    xs.append(x)
    val = (math.cosh(m*(L - x)) + (h/(m*k))*math.sinh(m*(L - x)))/(math.cosh(m*L) + (h/(m*k))*math.sinh(m*L))
    theta = val*50
    temp.append(theta + Tamb)
    x += 0.005

plt.plot(xs, temp)
plt.show()