from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque, modele, annee):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        
    @abstractmethod
    def cout_entretien_annuel(self):  
        return f"cout ici"
    
    def get_info(self):
        return f"{self.__marque}, {self.__modele}, {self.__annee}"
    
class Voiture(Vehicule):
    
    def cout_entretien_annuel(self):
        return f"500 € + 20 € par année depuis 2000"
    
class Moto(Vehicule):
    
    def cout_entretien_annuel(self):
        return f"300 € + 10 € par année depuis 2000"
    
class Camion(Vehicule):
    
    def cout_entretien_annuel(self):
        return "1000 € + 50 € par année depuis 2000"
    
voiture = Voiture("BMW", "Serie 3", 2020)
moto = Moto("Harley-Davidson", "Sportster 1000", 1977)
camion = Camion("Mack Trucks", "MH UltraLiner", 1982)

print(voiture.get_info())
print(voiture.cout_entretien_annuel())

print(moto.get_info())
print(moto.cout_entretien_annuel())

print(camion.get_info())
print(camion.cout_entretien_annuel())