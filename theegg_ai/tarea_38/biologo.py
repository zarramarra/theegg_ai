cadena1="ctgggccttgaggaaaactg"
cadena2="gtaccagtactgatagt"

cadena_mas_larga=""
i=0
while i<=(len(cadena1)-len(cadena_mas_larga)):   
    for j in range(i,len(cadena1)+1):
        if cadena1[i:j+1] in cadena2:
            if len(cadena1[i:j+1])>len(cadena_mas_larga):
                cadena_mas_larga = cadena1[i:j+1]
    i += 1

print("La cadena más larga encontrada es: ", cadena_mas_larga)