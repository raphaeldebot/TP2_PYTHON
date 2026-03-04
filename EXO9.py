entrer = input("Entrez quelquechose : ")

valide = True

for c in entrer:
    if not ("0" <= c <= "9"):
        valide = False

if valide:
    print("Cette entrer représente un nombre valide.")
else:
    print("Cette entrer n'est pas un nombre valide.")

    
n = input ("entrer un nombre svp : ")
print("Votre saisie est ok" if all("0" <= c <= "9" for c in n) else "Saisie contenant aumoins une valeur non numérique")