import numpy as np 

f = lambda x: x-2**(-x)

inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

a,b,erro = 0,1,10**(-5)
k = inter(a,b,erro)

for i in range(k):

    x = b -f(b)*(a-b)/(f(a)-f(b))

    if np.abs((x-b)/b)<erro:
        break
    
    a = b
    b = x 
    
print("Solução numérica: %f" %x)
print("Interações: %d" %i)