a=input("Entrez une lettre svp :")
if ord(a) >= ord("a") and ord(a) <= ord("z"):
    print ("Minuscule")
elif ord(a) >= ord("A") and ord(a) <= ord("Z"):
    print("MAJUSCULE")
else:
    print("C'est pas une lettre")
