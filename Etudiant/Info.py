
def nom():
    nom=input("Entrez votre nom:")
    return nom
def prenom():
    prenom=input("Entrez votre prenom:")
    return prenom
def age():
    age=int(input("Entrez votre age:"))
    if age>=18 :
        return age
    else:
        return "Votre age est infierieur a 18"
