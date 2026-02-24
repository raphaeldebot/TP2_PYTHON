saisie = input("Entrez un nombre entier : ")
nombre=0
for c in saisie:
     nombre = nombre * 10 + (ord(c)-ord("0")) 


nombreInverse = 0
nb_chiffres = len(saisie)

for i in range(nb_chiffres):
    chiffre = nombre % 10
    nombreInverse = nombreInverse * 10 + chiffre
    nombre = nombre // 10
    
print(nombreInverse)