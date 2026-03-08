class Voiture:
    def __init__(self, marque, modele, annee, vitesse):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse = vitesse
        
    def accelerer(self, valeur):
        self.vitesse += valeur
        print(f"{ self.marque} accelere -> {self.vitesse} km/h")
        
    def freiner(self):
        self.vitesse = 0
        print(f"{ self.marque} freine - à l'arret")
        
    def afficher(self):
        print(f"Année: {self.annee}, Marque: {self.marque}, Modele: {self.modele} - Vitesse: {self.vitesse} KM/h")
        print("Année: {self.annee}, Marque: {self.marque}, Modele: {self.modele} - Vitesse: {self.vitesse} KM/h")

    
voiture1 = Voiture("Toyota", "Yaris", "2022", 0)
voiture2 = Voiture("BMW", "X3", "2023", 0)

voiture1.accelerer(80)
voiture2.accelerer(120)

voiture1.afficher()
voiture2.afficher()