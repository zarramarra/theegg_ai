import numpy as np

# algoritmo para mostrar matriz: utilizado para debuggear
def Mostrar(matriz):
    print("La matriz es la siguiente:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

# bottom-up approach
def algoritmo_lechero_2(numero_vacas, peso_max, peso_vaca, litro_vaca):
    peso=range(0,peso_max+1)
    opciones = np.zeros((numero_vacas+1, peso_max+1),dtype=int)
    for i in range(1, numero_vacas+1):
        for j in range(1, peso_max+1):
            if peso_vaca[i-1] <= peso[j]:
                opciones[i][j] = max(opciones[i-1][j],opciones[i-1][j-peso_vaca[i-1]]+litro_vaca[i-1])
            else:
                opciones[i][j] = opciones[i-1][j]
    #Mostrar(opciones)
    return(np.amax(opciones))


l_peso_vaca=[1,2,5,6,7]
l_litro_vaca=[1,6,18,22,28]
num_vacas = len(l_peso_vaca)
peso_max = 11


litros_leche_max2 = algoritmo_lechero_2(num_vacas, peso_max, l_peso_vaca, l_litro_vaca)
print("La cantidad máxima de litros que puede obtener son ", litros_leche_max2, " litros.")