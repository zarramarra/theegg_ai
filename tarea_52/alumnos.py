# Programa para gestionar los nombres de alumnos de primaria y secundaria


def introducir_nombres():
    nuevo = 1
    curso = []
    while nuevo != "?x?":
        nuevo = input()
        if nuevo == "?x?":
            break
        curso.append(nuevo)
    return(curso)

def sin_repetir(curso):
    no_repe = []
    for i in range(len(curso)):
        if curso[i] not in no_repe:
            no_repe.append(curso[i])
    return no_repe

def nombres_repes(curso1, curso2):
    repetidos = []
    for i in range(len(curso1)):
        if curso1[i] not in repetidos:
            if curso1[i] in curso2:
                repetidos.append(curso1[i])
    return(repetidos)

def nombres_no_repes(curso1, curso2):
    no_repetidos = []
    for i in range(len(curso1)):
        if curso1[i] not in no_repetidos:
            if curso1[i] not in curso2:
                no_repetidos.append(curso1[i])
    for i in range(len(curso2)):
        if curso2[i] not in no_repetidos:
            if curso2[i] not in curso1:
                no_repetidos.append(curso2[i])
    return(no_repetidos)

print("**** 1. Crear lista alumnos primaria")
print("Ingrese los nombres de alumnos de primaria. Cuando no desee introducir más números introduzca un ?x?")
primaria = introducir_nombres()
print(primaria)
print("")

print("**** 2. Crear lista alumnos secundaria")
print("Ingrese los nombres de alumnos de secundaria. Cuando no desee introducir más números introduzca un ?x?")
secundaria = introducir_nombres()
print(secundaria)
print("")

print("**** 3. Mostrar nombres sin repetir")
primaria_no_repe = sin_repetir(primaria)
secundaria_no_repe = sin_repetir(secundaria)
print("primaria: ", primaria_no_repe)
print("secundaria: ", secundaria_no_repe)
print("")

print("**** 4. Mostrar nombres que se repiten en ambos cursos")
nombres_repetidos = nombres_repes(primaria,secundaria)
print(nombres_repetidos)
print("")

print("**** 5. Mostrar nombres que no se repiten en ambos cursos")
nombres_no_repetidos = nombres_no_repes(primaria,secundaria)
print(nombres_no_repetidos)
print("")
