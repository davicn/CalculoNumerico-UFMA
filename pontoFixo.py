import numpy as np


#f = lambda x: x-2**(-x)

# Função de interação
g = lambda x:-np.log(2)*2**(-x)

inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

a,b,erro = 0,1,10**(-5)
k = inter(a,b,erro)

cont=0
while True:
    x = g(b)
    print(x)
    if np.abs((x-b)/b)<erro:
        break
    b = x

print("Solução numérica: %f" %x)
#print("Interações: %d" %cont)