nombreInput1=input("Veuillez entrez un nombre svp : ")
nombreInput2=input("Veuillez entrez un deuxieme nombre svp : ")

res1=0
for c in nombreInput1:
    res1 = res1*10 + (ord(c)-ord("0")) 


res2=0
for c in nombreInput2:
    res2 = res2*10 + (ord(c)-ord("0")) 


print(res1 + res2)
