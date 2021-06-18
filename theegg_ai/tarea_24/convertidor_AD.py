def MostrarBinario(binario):
    str_binario = "".join([str(_) for _ in binario])
    str_0x_bin = "b"+str_binario
    print(str_0x_bin)



decimal = 256

n_bits = 0
n_bits_max = 16

if decimal>pow(2,n_bits_max)-1:
    print("Introduzca un numero mas pequeño!!!")
    print("Resolución máxima: ", n_bits_max, "bits. Valor máximo: ", pow(2,n_bits_max)-1)
else:
    j=0
    while n_bits<=0 and j<n_bits_max+1:
        if decimal < pow(2,j):
            n_bits = j
        j+=8
    
    #string binario
    binario = [0]*n_bits
    
    for i in range(n_bits-1):
        if decimal>=pow(2,n_bits-1-i):
            binario[i]=1
            decimal=decimal-pow(2,n_bits-1-i)
    #ultimo bit
    if decimal:
        binario[n_bits-1]=1
        
    MostrarBinario(binario)
