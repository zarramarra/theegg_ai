
# clase Persona

class Persona():
    def __init__(self):
        self._nombre = ""
        self._edad = ""
        self._dni = ""

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, n):
        if(n != ""):
            self._nombre = n
        else:
            print("El valor del nombre no es válido!")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, e):
        if (e >= 0):
            self._edad = e
        else:
            print("El valor de edad no es válido!")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, d):
        if (len(d) == 9):
            letra = d[8].upper()
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            num = d[:8]
            if ( len(num) == len( [n for n in num if n in "1234567890"] ) ):
                if tabla[int(num) % 23] == letra:
                    self._dni = d
        if(self._dni == ""):
            print("El valor del dni no es válido!")

    def mostrar(self):
        print("Nombre: ", self._nombre)
        print("Edad: ", self._edad)
        print("DNI: ", self._dni)

    def esMayorDeEdad(self):
        if self._edad >= 18:
            return True
        else:
            return False


p1 = Persona()
p1.nombre = "Ane"
p1.edad = 39
p1.dni = ""
p1.mostrar()
print(p1.esMayorDeEdad())