from Animal import Animal

class Vaca(Animal):
    def __init__(self, especie, edad, dueño):
        self.especie = especie
        self.edad = edad
        self.dueño = dueño
    def hablar(self):
        print("Muuu")
    def moverse(self):
        print("Caminando con 4 patas")