import sys


# Función que comprime un string utilizando el algoritmo L7ZZ

def comprimir(cadena):
    #invertir el string ya que el algoritmo LZ77 empieza desde el final del string
    cadena = cadena[::-1]
    #empezar a comprimir
    ventana = 1
    salida_comp = []
    salida_comp.append((0,0,cadena[0]))
    i=1

    while i < len(cadena):
        indice = cadena[0:i].rfind(cadena[i:i+ventana])
        if indice < 0:
            # Si no existe el caracter anteriormente, directamente añadimos una nueva línea con m=0 y n=0. El valor de S
            # será el siguiente caracter
            salida_comp.append((0,0,cadena[i]))
            i += 1
        else:
            # En caso de que exista el caracter que estamos analizando, hay que buscar si existe una ventana
            # mas larga que se repite
            nuevo_indice = indice
            while nuevo_indice >= 0:
                # bucle para encontrar la ventana más larga que se repite
                indice = nuevo_indice
                nuevo_indice = cadena[0:i].rfind(cadena[i:i+ventana])
                ventana += 1
                if ventana >= len(cadena)-indice or ventana>=i-indice or i+ventana-2<len(cadena):
                    # en caso de que se haya llegado al final del string --> salir del bucle
                    break
            salida_comp.append((i-indice,ventana-2,cadena[i+ventana-2]))
            i += ventana -1
        #inicializar la ventana para el siguiente caracter
        ventana = 1

    return salida_comp


# Función que descomprime una cadena comprimida utilizando el algoritmo L7ZZ
def descomprimir(comp):
    salida = ''
    i=0
    indice = 0
    while i < len(comp):
        m=comp[i][0]    # valor que nos dice cuánto tenemos que ir para atrás para encontrar el mismo/los mismos caracteres
        n=comp[i][1]    # valor que nos dice qué ventanta ocupa el caracter / los caracteres
        s=comp[i][2]    # siguiente caracter
        if m==0 and n==0:
            salida += s
            indice += 1
        else:
            salida += salida[indice-m:indice-m+n]+s
            indice +=1+n
        i += 1
    #volver a voltear el string y devolverlo
    salida = salida[::-1]
    return salida



# 1.Recoger cadena de máximo 30 caracteres

print("introduzca una cadena de caracteres como máximo de longitud 30: ")
cadena_inicial = input()
longitud = len(cadena_inicial)
while longitud > 30:
    print("la cadena es más larga que 30 caracteres!")
    print("introduzca otra cadena (más corta que 30 caracteres):")
    cadena_inicial = input()
    longitud = len(cadena_inicial)


# 2.Print mostrando el espacio de memoría del string introducido
print(cadena_inicial, "--> el espacio de memoria del string inicial es de ", sys.getsizeof(cadena_inicial), " bytes")
print(len(cadena_inicial))

# 3.Comprimir el string
cadena_comp = comprimir(cadena_inicial)

# 4.Print mostrando el espacio de memoría del string comprimido
print("El espacio de memoria del string comprimido es de ", sys.getsizeof(cadena_comp), " bytes")
print(cadena_comp)

# 5.Decomprimir el string comprimido
cadena_descomp = descomprimir(cadena_comp)

# 2.Print mostrando el espacio de memoría del string descomprimido
print(cadena_descomp, "--> el espacio de memoria del string descomprimido es de ", sys.getsizeof(cadena_inicial), " bytes")
