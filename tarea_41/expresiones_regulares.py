import re
import operator

# Definir el texto y el número de palabras más frecuentes a mostrar en pantalla
texto = "En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie.Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."
n_mas_frecuentes = 10

frecuencia_palabras = {}

# Expresiones regulares para encontrar palabras y caracteres
lista_palabras = (re.findall(r'\w+',texto))
lista_caracteres = (re.findall(r'.',texto))

# Obtener el numero de palabras y caracteres
num_palabras = len(lista_palabras)
num_caracteres = len(lista_caracteres)

# Obtener la frecuencia de aparición de cada palabra
for palabra in lista_palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Ordenar las palabras en función de la frecuencia de aparición
ranking_palabras = sorted(frecuencia_palabras.items(), key=operator.itemgetter(1), reverse=True)

# Mostrar resultados
print(f"El número de palabras del texto es: {num_palabras}")
print(f"El número de caracteres del texto es: {num_caracteres}")
print(f"Las {n_mas_frecuentes} palabras más frecuentes son: {ranking_palabras[0:n_mas_frecuentes]}")

