# Programa para gestionar listas de numeros

lista = []
nuevo = 1

print("**** 1. Crear lista ******************************************************************")
print("ingrese elementos en una lista. Cuando no desee introducir más números introduzca un 0")
while nuevo != 0:
    nuevo = int(input())
    if nuevo == 0:
        break
    lista.append(nuevo)

print(lista)
print("")


print("**** 2. Eliminar elemento lista *********************************************************")
print(" ingrese un número para eliminiarlo de la lista ")
eliminar = int(input())
if eliminar in lista:
    lista.remove(eliminar)
    print("se ha eliminado el primer ",  eliminar, " encontrado de la lista!")
    print(lista)
else:
    print("el número introducido no está en la lista")
    print(lista)
print("")

print("**** 3. Sumatorio lista ******************************************************************")
print("Ahora vamos a calcular el sumatorio de toda la lista: ")
suma = 0
for i in range(len(lista)):
    suma += lista[i]
print("suma de toda la lista: ", suma)
print("")

print("**** 4. Nueva lista con valores menores que X *******************************************")
print("introduzca un numero para evaluar cuántos son menores en la lista:")
max_num = int(input())
lista_menores = []
for i in range(len(lista)):
    if lista[i] < max_num:
        lista_menores.append(lista[i])
print("nueva lista: ", lista_menores)
print("")

print("**** 5. Crear lista (elemento, nºveces) **************************************************")
print("vamos a calcular cuántas veces aparece cada elemento de la lista:")
lista_veces = []
numeros = []
for i in range(len(lista)):
    if lista[i] not in numeros:
        lista_veces.append([lista[i], lista.count(lista[i])])
        numeros.append(lista[i])
print(lista_veces)
print("")
