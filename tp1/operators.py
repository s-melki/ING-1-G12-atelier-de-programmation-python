x = 20
#print(x)
x = "saber"
#print(x)

# ça marche parce que le variable x est décalrée en statique non dynamique
i = 0

fruits = ["pomme", "banane", "orange"]
    
fruits.append("kiwi") # append ajoute a la fin du tableau
fruits[2] = "cerise"
fruits.insert(7, "cerise 2") # ajouter une valeur a un indice donnée

print(fruits[4])
for i in fruits:
    print(i)


