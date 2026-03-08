class Bibliotheque:

    def __init__(self, nom):
        self.nom = nom
        self.__livres = []

    @property
    def nb_livres(self):
        return len(self.__livres)

    def ajouter_livre(self, titre):
        if titre not in self.__livres:
            self.__livres.append(titre)
            print(f'"{titre}" ajouté.')
        else:
            print(f'"{titre}" est déjà dans la bibliothèque.')

    def retirer_livre(self, titre):
        if titre in self.__livres:
            self.__livres.remove(titre)
            print(f'"{titre}" retiré.')
        else:
            print(f'"{titre}" introuvable.')

    def afficher_livres(self):
        print(f"=== {self.nom} ({self.nb_livres} livres) ===")
        for i, l in enumerate(self.__livres, 1):
            print(f"{i}. {l}")


# Utilisation
bib = Bibliotheque("Ma Bibliothèque")

bib.ajouter_livre("Le Petit Prince")
bib.ajouter_livre("1984")
bib.ajouter_livre("Le Petit Prince")  # déjà présent

bib.afficher_livres()

print(bib.nb_livres)  # 2