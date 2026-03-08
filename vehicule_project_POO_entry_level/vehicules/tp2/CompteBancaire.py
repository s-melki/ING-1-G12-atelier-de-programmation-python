class CompteBancaire:

    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire
        self.__solde = solde_initial  # attribut privé

    # ── GETTER ──────────────────────────────
    @property
    def solde(self):
        """Lecture du solde."""
        return self.__solde

    # ── SETTER ──────────────────────────────
    @solde.setter
    def solde(self, valeur):
        """Modification contrôlée."""
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif !")
        self.__solde = valeur

    # ── Méthodes métier ─────────────────────
    def deposer(self, montant):
        if montant <= 0:
            print("Montant invalide.")
            return

        self.__solde += montant
        print(f"Dépôt de {montant}€ → solde: {self.__solde}€")

    def retirer(self, montant):
        if montant > self.__solde:
            print("Solde insuffisant !")
            return

        self.__solde -= montant
        print(f"Retrait de {montant}€ → solde: {self.__solde}€")

    def __str__(self):
        return f"Compte de {self.titulaire} : {self.__solde}€"


# ── Utilisation ───────────────────────────

compte = CompteBancaire("Alice", 1000)

print(compte.solde)      # 1000 (via le getter)

compte.deposer(500)     # Dépôt de 500€ → solde: 1500€
compte.retirer(200)     # Retrait de 200€ → solde: 1300€

#compte.__solde         # AttributeError ! attribut privé
#compte.solde = -500    # ValueError ! setter contrôle