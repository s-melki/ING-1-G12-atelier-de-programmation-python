
from animal import Animal


class Chien(Animal):
    def __init__(self, nom, age, prix, race, est_dresse, ):
        super().__init__(nom, age, prix)
        self.race =race
        self.est_dresse = est_dresse

    def parler(self):
        print (f"{self.nom} dit: Woof!")    
    
    def decrire(self):
        print(f"{self.nom} est un {self.race} de {self.age} ans. Dressé: {'Oui' if self.est_dresse else 'Non'}.")

    def faire_la_patte(self):
        print(f"{self.nom} fait la patte!")
        
    