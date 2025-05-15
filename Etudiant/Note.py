

def note():
    nb = int(input("Siaser votre nombre de module:"))
    listeNote = []
    i=0
    while i<nb:
        note=float(input("Entrez note de module:"))
        listeNote.append(note)
        i+=1
    return listeNote



