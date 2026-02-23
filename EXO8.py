nombre = input('veuillez entrer un nombre')

resint=0
for c in nombre:
    resint = resint * 10 + int(c) 

resord=0
for c in nombre:
    resord = resord * 10 + (ord(c)-ord("0")) 


print(resint)
print(resord)
print(nombre)
