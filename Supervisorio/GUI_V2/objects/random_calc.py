import controlpy
import numpy as np


A = 4
B = 1
hm = 4
rho = 1000
g = 9.8
k = 0.001
'''
h1ss = 1
h2ss = 1
u1ss = 0
u2ss = k*math.sqrt(rho*g)

gamma = (A-B)/(2*hm)
beta = 4/(4*pi*pow(gamma*h1ss,2) + 4*B*gamma*h1ss + pow(B,2))
dbeta = -4*(8*pi*pow(gamma,2)*h1ss + 4*gamma*B)/pow((4*pi*pow(gamma*h1ss,2) + 4*B*gamma*h1ss + pow(B,2)),2)

A = -(dbeta*k*sqrt(rho*g*h1ss)+beta*k*sqrt(rho*g)/(2*sqrt(h1ss)))
B = beta*k*sqrt(rho*g)/(2*sqrt(h1ss))
print(k*sqrt(rho*g*2.5))'''

A = np.matrix([[-0.063, 0.046],[0, -0.063]])
B = np.matrix([[0.937, 0],[0, 0.937]])
Q = np.matrix([[0.5, 0],[0, 0.5]])
R = np.matrix([[0.5, 0],[0, 0.5]])
input_data = [1, 2]
K, P, e = controlpy.synthesis.controller_lqr(A, B, Q, R)
#K = [list(gain[0]) for gain in list(K)]
print(K.tolist())
exit()
signals = 	[input_data[0]*K[0][0] + input_data[1]*K[0][1],
			input_data[0]*K[1][0] + input_data[1]*K[1][1]]
print(signals)