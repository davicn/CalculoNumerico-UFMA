# Método da falsa posição

import numpy as np 


f = lambda x: x-2**(-x)

inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

a,b,erro = 0,1,10**(-5)
k = inter(a,b,erro)

x = (a*f(b)-b*f(a))/(f(b)-f(a))

for i in range(k):
    if np.abs(f(x)) >= erro:
        if f(a)*f(x)<0:
            b = x
        else:
            a = x
    else:
        break

print("Solução numérica: %f" %x)
print("Interações: %d" %i)
