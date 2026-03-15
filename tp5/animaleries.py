class Animaleries:
    def __init__(self, nom):
        self.nom = nom
        self.animals = []

    def ajouter_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        print(f"Animaleries: {self.nom}")
        for animal in self.animals:
            print(f"- {animal}")

    def vendre_animal(self, animal):
        if animal in self.animals:
            prix = animal.vendre()
            self.animals.remove(animal)
            print(f"{animal.nom} a été vendu pour {prix} euros.")
        else:
            print(f"{animal.nom} n'est pas disponible à la vente.")

    def nb_animaux(self):
        return len(self.animals)
    
    def afficher_catalogue(self):
        print(f"Catalogue de l'animalerie {self.nom}:")
        for animal in self.animals:
            animal.decrire()

    def rechercher_par_type(self, type_animal):
        print(f"Recherche de {type_animal} dans l'animalerie {self.nom}:")
        for animal in self.animals:
            if isinstance(animal, type_animal):
                animal.decrire()

    def statistiques(self):
        stats = {}
        for animal in self.animals:
            type_animal = type(animal).__name__
            stats[type_animal] = stats.get(type_animal, 0) + 1
        print(f"Statistiques de l'animalerie {self.nom}:")
        for type_animal, count in stats.items():
            print(f"{type_animal}: {count}")




    