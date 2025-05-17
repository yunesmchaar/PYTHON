import numpy
import random

def jeurs():
        # --- Initialisation des données ---
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        habitudes = ["Sport à 5h", "Lecture", "Méditation 10min","cours dans bibloitheque"]
        suivi = {jour: {h: False for h in habitudes} for jour in jours}

        # --- Saisie des activités ---
        print("=== Suivi de tes habitudes pour la semaine ===\n")
        for jour in jours:
            print(f"\n📅 {jour}")
            for habitude in habitudes:
                reponse = input(f"→ As-tu fait « {habitude} » ? (o/n) : ").strip().lower()
                if reponse == "o":
                    suivi[jour][habitude] = True

        # --- Résumé de la semaine ---
        print("\n=== Résumé de ta semaine ===\n")
        total = 0
        faits = 0

        for jour in jours:
            print(f"📆 {jour} :")
            for habitude, fait in suivi[jour].items():
                etat = "✅" if fait else "❌"
                print(f"  - {habitude} : {etat}")
                total += 1
                if fait:
                    faits += 1
            print()

        pourcentage = (faits / total) * 100
        print(f"🎯 Taux de réussite hebdomadaire : {faits}/{total} = {pourcentage:.2f}%")

        # --- Message motivation ---
        if pourcentage >= 85:
            print("💪 Excellent travail ! Tu es sur la bonne voie 🔥")
        elif pourcentage >= 60:
            print("👍 Bon début, continue comme ça !")
        else:
            print("👀 Essaie d’être plus régulier la semaine prochaine.")

jeurs()