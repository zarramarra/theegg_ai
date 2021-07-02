

## 1. Algoritmo para ORDENAR la lista de menor a mayor
def ordenar_lista(lista):
    # eliminar numeros repetidos
    lista = list(set(lista)) 
    
    # ordenar la lista
    for i in range(0, len(lista)-1):
        if lista[i]>min(lista[i+1:len(lista)]):
            min_position = lista.index(min(lista[i+1:len(lista)]))
            aux = lista[min_position]
            lista[min_position] = lista[i]
            lista[i] = aux
    return(lista)

## 2.a) Búsqueda SECUENCIAL
def busqueda_secuencial(num, lista):
    it_sec = 0
    for i in range(0,len(lista)):
        it_sec+=1
        if num == lista[i]:
            return (i,it_sec)
    return(-1,it_sec)
            
## 2.b) Búsqueda BINARIA
def busqueda_binaria(num, lista):
    it_bin = 0
    min_ind = 0
    center_ind = 1
    max_ind = len(lista)
    while(center_ind > 0 and center_ind < len(lista)-1):
        it_bin+=1
        center_ind = (max_ind+min_ind)//2
        if (num>lista[center_ind]):
            min_ind = center_ind
        elif (num<lista[center_ind]):
            max_ind = center_ind
        else:
            return(center_ind, it_bin)
    return(-1,it_bin)
    
## MAIN - PROGRAMA PRINCIPAL ##########################################
lista = [3,56,21,33,874,123,66,1000,23,45,65,56]   
num = 123 

# ordenar y mostrar lista
lista = ordenar_lista(lista)
print("Lista ordenada:",lista)
print("Número a encontrar:", num)

# aplicar ambos algoritmos de búsqueda
[ind_sec, it_sec] = busqueda_secuencial(num, lista)
[ind_bin, it_bin] = busqueda_binaria(num, lista)

# mostrar resultados
if (ind_sec >= 0):
    print("SECUENCIAL --> Posición: ", ind_sec, "(numero de iteraciones:", it_sec, ")")
else:
    print("SECUENCIAL --> Número no encontrado (numero de iteraciones:", it_sec, ")")

if (ind_bin >= 0):
    print("BINARIA --> Posición: ", ind_bin, "(numero de iteraciones:", it_bin, ")")
else:
    print("BINARIA --> Número no encontrado (numero de iteraciones:", it_bin, ")")
