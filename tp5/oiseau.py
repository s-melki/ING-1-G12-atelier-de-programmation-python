
from animal import Animal


class Oiseau(Animal):
    def __init__(self, nom, age, prix, espece, peut_voler):
        super().__init__(nom, age, prix)
        self.espece = espece
        self.peut_voler = peut_voler

    def parler(self):
        print (f"{self.nom} dit: Wit Wit!")    
    
    def decrire(self):
        print(f"{self.nom} est un {self.espece} de {self.age} ans. Peut voler: {'Oui' if self.peut_voler else 'Non'}.")

    def chanter(self):
        print(f"{self.nom} chante une mélodie joyeuse.")