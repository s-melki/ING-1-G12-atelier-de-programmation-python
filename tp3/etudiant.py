class Etudiant:
    # Attribut de classe (partagé)
    etablissement = "Université de Lyon"
    nb_etudiants = 0  # compteur global

    def __init__(self, nom, note):
        # Attributs d'instance (propres à chaque étudiant)
        self.nom = nom
        self.note = note
        Etudiant.nb_etudiants += 1  # on incrémente le compteur de classe

    def statut(self):
        mention = "Admis" if self.note >= 10 else "Ajourné"
        print(f"{self.nom} : {self.note}/20 → {mention}")


# Création des étudiants
e1 = Etudiant("Alice", 15)
e2 = Etudiant("Bob", 8)
e3 = Etudiant("Clara", 12)

# Attribut de classe → même valeur pour tous
e1.etablissement = "abc"
print(e1.etablissement)       # Université de Lyon
print(Etudiant.nb_etudiants)  # 3

# Attributs d'instance → valeurs différentes
print(e1.nom, e1.note)  # Alice 15
print(e2.nom, e2.note)  # Bob 8