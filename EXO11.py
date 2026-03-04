

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

n=input("Faites entrer un nombre svp")
res=0
exp=-1
for c in n:
     a=ord(c)-ord("0")
     res = res*10+a
     exp+=1


for i in range(exp,-1,-1):
     print(res//(10**i))
     res = (res%(10**i))