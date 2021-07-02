import time

cantidad = 1000000


def suma_lineal(num):
    resultado = 0
    for i in range(0,num+1):
        resultado += i
    return resultado

def suma_constante(num):
    return((num+1)*(num//2)) 

for i in range(4):
    t0 = time.time()
    suma1 = suma_lineal(cantidad)
    t1 = time.time()
    suma2 = suma_constante(cantidad)
    t2 = time.time()
    
    print("{}   -   {}".format(suma1, t1-t0))
    print("{}   -   {}".format(suma2, t2-t1))
    
    cantidad *= 10

