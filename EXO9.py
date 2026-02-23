texte = input("Entrez un texte : ")

valide = True

for c in texte:
    if not ("0" <= c <= "9"):
        valide = False

if valide:
    print("Ce texte représente un nombre valide.")
else:
    print("Ce texte n'est pas un nombre valide.")