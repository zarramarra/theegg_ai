
num = float(input("Introduzca un decimal (no más de 4 cifras decimales) para hallar su fracción indivisible: "))
denominador = 10000
numerador = num * denominador
numerador = int(numerador)

idx = 1

while idx<=denominador:
    idx = idx + 1
    if not(numerador % idx):
        if not(denominador % idx):
            numerador = numerador // idx
            denominador = denominador // idx
            idx = 1;

print("La fracción indivisible de ", num, " es ", numerador,"/",denominador)