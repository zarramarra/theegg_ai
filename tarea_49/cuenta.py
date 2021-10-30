
# clase Cuenta
class Cuenta():
    def __init__(self, titular):
        self._titular = titular
        self._cantidad = 0

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nuevo_titular):
        if(nuevo_titular != ""):
            self.titular = nuevo_titular
        else:
            print("El valor del titular no es válido!")

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cant):
        if isinstance(cant, float) or isinstance(cant, int):
            self.cantidad = cant
        else:
            print("El valor de cantidad no es válido!")


    def mostrar(self):
        print(" Titular: ", self.titular)
        print(" Cantidad: ", self._cantidad)

    def ingresar(self, cantidad):
        self._cantidad = self._cantidad + cantidad

    def retirar(self, cantidad):
        if self._cantidad < 0:
            return (print("Cuenta en números rojos, no se puede retirar dinero!"))
        self._cantidad = self._cantidad - cantidad


c1 = Cuenta("Ane")
c1.mostrar()
c1.ingresar(100.0)
c1.mostrar()
c1.ingresar(1100)
c1.mostrar()
c1.retirar(150)
c1.mostrar()
c1.retirar(1500)
c1.mostrar()
c1.retirar(1500)
c1.mostrar()