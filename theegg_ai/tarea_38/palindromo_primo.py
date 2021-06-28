# Funcion que determina si un numero es primo
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

# Funcion que determina si un numero es palindromo     
def es_palindromo(num):
    digitos = str(num)
    num_digitos = len(digitos)
    for i in range(0,int(num_digitos//2)):
        if digitos[i] != digitos[num_digitos-i- 1]:
           return False
    return True

# Funcion que encuentra introuciendo un numero N, el numero menor que sea primo y palindromo y que sea mayor o igual que N
def palindromo_primo(num):
    for n in range(num,10000000):
        if es_palindromo(n):
            if es_primo(n):
                return n
    return -1

num = 456789
#num = 31
#num = 999999

print("La respuesta es:", palindromo_primo(num))  