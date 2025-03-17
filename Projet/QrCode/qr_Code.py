import qrcode


def generer_qrcode(texte, nom_fichier="qrcode.png"):
    # Création du QR Code
    qr = qrcode.QRCode(
        version=1,  # Taille du QR Code (1 à 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
        box_size=10,  # Taille des cases
        border=4,  # Taille de la bordure
    )

    qr.add_data(texte)
    qr.make(fit=True)

    # Génération de l'image
    img = qr.make_image(fill="black", back_color="white")

    # Sauvegarde de l'image
    img.save(nom_fichier)
    print(f"QR Code enregistré sous le nom : {nom_fichier}")


# Exécuter la fonction
texte_a_encoder = input("Entrez le texte ou l'URL à encoder : ")
generer_qrcode(texte_a_encoder)

