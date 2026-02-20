texte=input("Entrez un texte svp")
res=0
for c in texte:
    if "0"<=c<="9":
        res+=1
print(res)