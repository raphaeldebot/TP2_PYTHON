

saisie = input("Entrez un nombre entier : ")
# nombre = int(saisie)
nombre=0
for c in saisie:
     nombre = nombre * 10 + (ord(c)-ord("0")) 
nb_chiffres = len(saisie)

for i in range(nb_chiffres):
    chiffre = nombre % 10
    print(chiffre)
    nombre = nombre // 10