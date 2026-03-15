
from animal import Animal

class Chat(Animal):
    def __init__(self, nom, age, prix,longeur_poils,interieur):
        super().__init__(nom, age, prix)
        self.longeur_poils = longeur_poils
        self.interieur = interieur

    def parler(self):
        print (f"{self.nom} dit: Meow!")    
    
    def decrire(self):
        print(f"{self.nom} est {self.age} ans. Longeur des poils: {self.longeur_poils}. Intérieur: {'Oui' if self.interieur else 'Non'}.")

    def ronronner(self):
        print(f"{self.nom} ronronne doucement.")