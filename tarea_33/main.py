class Personaje:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.vida = 100
        self.ataque = ataque

    def win(self):
        print(self.nombre + " ha ganado!!")


pikachu = Personaje('Pikachu', 5)
jigglypuff = Personaje('Jigglypuff', 6)

turno = 1

while pikachu.vida > 0 and jigglypuff.vida > 0:
    if turno:
        jigglypuff.vida = jigglypuff.vida - pikachu.ataque
        turno = 0
    else:
        pikachu.vida = pikachu.vida - jigglypuff.ataque
        turno = 1

if pikachu.vida <= 0:
    jigglypuff.win()
else:
    pikachu.win()
