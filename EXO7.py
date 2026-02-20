nombreInput=input("Veuillez entrez un nombre svp : ")
res=0
for c in nombreInput:
    res = res*10 + (ord(c)-ord("0")) 
print(res)