from Animal import Animal

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        self.especie = especie
        self.edad = edad
        self.dueño = dueño
    def hablar(self):
        print("goaos")
    def moverse(self):
        print("corriendo")
