

def algoritmo_lechero(numero_vacas, peso_max, peso_vaca, litro_vaca):
    anterior = [0] * (peso_max+1)
    actual = [0] * (peso_max+1)
    peso=range(0,peso_max+1)
    for i in range(1, numero_vacas+1):
        peso_camion = 0
        for j in range(1, peso_max+1):
            #vamos a seleccionar la vaca i-1 
            if peso_vaca[i-1] <= peso[j]:
                actual[j]=max(anterior[j],actual[j-peso_vaca[i-1]]+litro_vaca[i-1])
            else:
                actual[j]=anterior[j]
        anterior = actual[:]
    return(max(actual))
    

# ------------------------------------------------- #  
# Programa principal
# ------------------------------------------------- #  

# Datos para el algoritmo
l_peso_vaca=[1,2,5,6,7]
l_litro_vaca=[1,6,18,22,28]
num_vacas = len(l_peso_vaca)
peso_max = 11

# Algoritmo lechero
litros_leche_max = algoritmo_lechero(num_vacas, peso_max, l_peso_vaca, l_litro_vaca)
print("La cantidad máxima de litros que puede obtener son ", litros_leche_max, "litros.")