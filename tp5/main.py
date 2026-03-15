

from oiseau import Oiseau
from chat import Chat
from chien import Chien
from animal import Animal
from animaleries import Animaleries

a1=Oiseau("Perrine", 2, 50, "Perruche", True)
a2=Chat("Siamois", 3, 30, "Meow", "Gris")
a3=Chien("Rex", 5, 100, "Berger Allemand", "Noir et feu")
a4=Chien("Bobi", 5, 100, "Berger Allemand", "Noir et feu")

""" a1.decrire()
a2.decrire()
a3.decrire()

a1.parler()
a2.parler()
a3.parler()

a1.chanter()
a2.ronronner()
a3.faire_la_patte() 

a1.vendre()
a2.vendre() 
a3.vendre()"""

mar=Animaleries("Le Paradis des Animaux")
mar.ajouter_animal(a1)
mar.ajouter_animal(a2)
mar.ajouter_animal(a3)
mar.ajouter_animal(a4)

#mar.display_animals()

#mar.afficher_catalogue()

#mar.rechercher_par_type(Chien)

mar.nb_animaux()

mar.statistiques()