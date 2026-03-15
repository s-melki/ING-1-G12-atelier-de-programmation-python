from abc import ABC, abstractmethod


class Animal(ABC):
    nb_animaux = 0
    def __init__(self, nom,age,prix):
        self.nom = nom
        self.age = age
        self.__prix = prix
        Animal.nb_animaux += 1

    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self, value):
        if value < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        self.__prix = value


    @abstractmethod
    def parler(self):
        pass

    @abstractmethod
    def decrire(self):
        pass     

    def vendre(self):
        print(f"{self.nom} a été vendu pour {self.prix} euros.")
        return self.prix
    
    def __str__(self):
        return f"{self.nom} ({self.age} ans) - Prix: {self.prix} euros"
    
    def __repr__(self):
        return f"Animal(nom={self.nom!r}, age={self.age!r}, prix={self.prix!r})"
    


     


