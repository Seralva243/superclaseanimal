from Animal import Animal
class Abeja(Animal):
    def __init__(self, especie, edad, dueño):
        self.especie = especie
        self.edad = edad
        self.dueño = dueño
    def hablar(self):
        print("Bzzzz")
    def moverse(self):
        print("Volando")
    def picar(self):
        print("Picar")