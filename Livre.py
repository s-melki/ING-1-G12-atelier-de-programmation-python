class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        
    def __str__(self):
        return f'"{self.titre}" par {self.auteur} ({self.pages} p.)'
    
    def __repr__(self):
        return f"Livre(titre={self.titre!r}, auteur={self.auteur!r})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, autre):
        return self.titre == autre.titre and self.auteur == autre.auteur
    
l1 = Livre("Le Petit Prince", "Saint-Exupéry", 96)
l2 = Livre("1984", "Orwell", 328)
print(l1) # "Le Petit Prince" par Saint-Exupéry (96 p.)
print(len(l2)) # 328
print(l1 == l2) # False