


frases=["this is a test", "foobar", "all your base"]

def invertir_palabras(num_frases, frases):
    for i in range(0,num_frases):
        palabras = frases[i].split()
        nueva_cadena = ""
        num_palabras = len(palabras)
        for j in range(0, num_palabras):
            nueva_cadena = nueva_cadena + palabras[num_palabras-j-1] + " "
        print("Case #", i+1, ": ", nueva_cadena)


n_frases = len(frases)
invertir_palabras(n_frases, frases)