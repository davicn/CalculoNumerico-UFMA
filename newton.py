import numpy as np 
from scipy.misc import derivative


f = lambda x: x-2**(-x)

inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

a,b,erro = 0,1,10**(-5)
k = inter(a,b,erro)

for i in range(k):
    x = a-(f(a)/derivative(f,a))

    if np.abs((x-a)/a)<erro:
        break
    a = x

print("Solução numérica: %f" %x)
print("Interações: %d" %i)