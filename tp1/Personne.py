class Personne:
    
    etablissement = "iTeam University"
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        
    def se_presenter(self):
        print(f"Bonjour, je suis {self.prenom} {self.nom}, j'ai {self.age} ans.") 
        
    def est_majeur(self):
        return self.age >= 18
    
p1 = Personne("Dupont", "Alice", 25)
p2 = Personne("Martin", "Bob", 16)

p1.se_presenter()
p2.se_presenter()


print(p1.etablissement)
print(p2.etablissement)

print(p1.est_majeur())
print(p2.est_majeur())

print('--------------------------------------------')
ps = [p1, p2]

for p in ps:
    p.se_presenter()
    print(p.est_majeur())
    