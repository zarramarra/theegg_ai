import random

# VARIABLES GLOBALES
cod_letra = list(map(chr, range(65, 91)))   # Listado caracteres
cod_valor = range(1,27)                     # Valor correspondiente a cada caracter

# --------------------------------------------------------------------------------------------- 
# FUNCION: cifrar_con_solitario()  --> introduciendo un str de entrada y la baraja (clave) se cifra el str de entrada 
def cifrar_con_solitario(plain_text,baraja):
    arr_pl_tx = []
    ciphred_ch_arr=[]
    # 1. Pasar el texto a su codificacion numerica
    for idx in range(len(plain_text)):
        if plain_text[idx] != " ":
    	    new_el = cod_valor[cod_letra.index(plain_text[idx])]
    	    arr_pl_tx.append(new_el)
    
    # 2. Aplicar el algoritmo del solitario al texto codificado
    for i in range(len(arr_pl_tx)):
        ch = arr_pl_tx[i]
        [num_to_add,baraja] = alg_solitario(baraja)
        ciphred_num = arr_pl_tx[i] + num_to_add
    
        while ciphred_num >26:
            ciphred_num=ciphred_num-26
        ciphred_ch = cod_letra[cod_valor.index(ciphred_num)]
        ciphred_ch_arr.append(ciphred_ch)
        
    # 3. Devolver la cadena cifrada
    ciphred_str = "".join(ciphred_ch_arr)
    return ciphred_str
# --------------------------------------------------------------------------------------------   

# ---------------------------------------------------------------------------------------------
# FUNCION: decifrar_con_solitario()  --> introduciendo un str de entrada y la baraja (clave) se decifra el str de entrada que es un mensaje cifrado   
def decifrar_con_solitario(ciphred_text,baraja):
    rx_data = []
    deciphred_ch_arr = []
    # 1. Pasar el texto a su codificacion numerica
    for idx in range(len(ciphred_text)):
        if ciphred_text[idx] != " ":
    	    new_el = cod_valor[cod_letra.index(ciphred_text[idx])]
    	    rx_data.append(new_el)

    # 2. Aplicar el algoritmo del solitario al texto codificado
    for i in range(len(rx_data)):
        [num_to_rest,baraja] = alg_solitario(baraja)
        deciphred_num = rx_data[i] - num_to_rest
    
        while deciphred_num <= 0:
            deciphred_num=deciphred_num+26
        deciphred_ch = cod_letra[cod_valor.index(deciphred_num)]
        deciphred_ch_arr.append(deciphred_ch)
        
    # 3. Devolver cadena decodificada
    deciphred_str = "".join(deciphred_ch_arr)
    return deciphred_str
# --------------------------------------------------------------------------------------------  

# --------------------------------------------------------------------------------------------- 
# FUNCION: alg_solitario --> algoritmo para obtener el keystream del solitario 
def alg_solitario(baraja): 
    # 1. Buscar JokerA y llevar una posicion atras
    idx_jokerA = baraja.index(53)
    if idx_jokerA < len(baraja)-1:
        new_idx_jokerA = idx_jokerA+1
    else:   #si esta en la ultima posicion
        new_idx_jokerA = 0
    temp = baraja[idx_jokerA] 
    baraja[idx_jokerA] = baraja[new_idx_jokerA]
    baraja[new_idx_jokerA] = temp

    # 2. Buscar JokerB y llevar dos posiciones atras
    idx_jokerB = baraja.index(54)
    if idx_jokerB < len(baraja)-2:
        new_idx_jokerB = idx_jokerB+2
        idx_middle = idx_jokerB+1
    elif idx_jokerB < len(baraja)-1:
        new_idx_jokerB = 0
        idx_middle = len(baraja)-1
    else:
        new_idx_jokerB = 1
        idx_middle = 0
    temp = baraja[idx_jokerB] 
    baraja[idx_jokerB] = baraja[idx_middle]
    baraja[idx_middle] = baraja[new_idx_jokerB]
    baraja[new_idx_jokerB] = temp
    
    # 3. Triple corte: primero vamos a saber cual de los comodines es el primero
    if new_idx_jokerA < new_idx_jokerB:
        first_joker = new_idx_jokerA
        second_joker = new_idx_jokerB
    else:
        first_joker = new_idx_jokerB
        second_joker = new_idx_jokerA
    baraja_corte1 = baraja[second_joker+1:len(baraja)]+baraja[first_joker:second_joker+1]+baraja[:first_joker]
    
    # 4. Corte de numero
    last_card = baraja_corte1[len(baraja_corte1)-1]
    if last_card == 54:
        last_card = 53
    baraja_corte2 = baraja_corte1[last_card:len(baraja_corte1)-1]+baraja_corte1[:last_card]
    baraja_corte2.append(baraja_corte1[len(baraja_corte1)-1])
    
    # 5. Key del keystream
    output_card = baraja_corte2[0]
    if output_card == 54:
        output_card = 53
    return (baraja_corte2[output_card],baraja_corte2)
# -------------------------------------------------------------------------------------------- 

# ---------------------------------------------------------------------------------------------
# FUNCION: mezclar_baraja() --> mezcla la baraja de forma aleatoria
def mezclar_baraja(baraja_orig):
    baraja = baraja_orig[:]
    for i in range(len(baraja)):
        idx_aleat = random.randint(0, len(baraja) - 1)
        temp = baraja[i]
        baraja[i] = baraja[idx_aleat]
        baraja[idx_aleat] = temp
    return baraja
# -------------------------------------------------------------------------------------------- 

## -------------------------------------------------------------------------------------------
## PROGRAMA PRINCIPAL
## --------------------------------------------------------------------------------------------
# 1. Introducir la cadena de caracteres
print("Introduzca el mensaje secreto (a-z y A-Z) para codificar: ")
plain_text_in = input()
plain_text = plain_text_in.upper()

# 2. Preparar las barajas para el emisor y el receptor (cifrado y descifrado)
baraja = list(range(1,55))
baraja = mezclar_baraja(baraja)
baraja_tx = baraja[:]
baraja_rx = baraja[:]

# 3. Funcion de cifrado
ciphred_str = cifrar_con_solitario(plain_text,baraja_tx)

# 4. Funcion de decifrado
deciphred_str = decifrar_con_solitario(ciphred_str, baraja_rx)

# 5. Mostrar cadena: original, cifrada y decifrada
print("Cadena original", plain_text)
print("Cadena cifrada", ciphred_str)
print("Cadea descifrada:", deciphred_str)

#----------------------------------------------------------------------------------------------


