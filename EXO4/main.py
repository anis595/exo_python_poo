from classes.Imprimante3D import Imprimante3D
from classes.Atelier3D import Atelier3D

ipe = Imprimante3D("237287", "P2S", "bambulab", 2025, True)
mon_atelier = Atelier3D("Mon atelier")


while True:
    print(
        "1. Ajouter une imprimante\n2. Retirer une imprimante\n3 .Afficher les imprimantes\n4. Chercher une imprimante par marque\n5. Imprimante disponible\n0 .QUITTER"
    )
    choix = int(input(" Quel est votre choix ? "))
    if choix == 1:
        numero = input("Numéro de série :")
        model = input("Modele :")
        marque = input("Marque :")
        annee = input("Année :")
        nouvelle_imprimante = Imprimante3D(numero, model, marque, annee)
        mon_atelier.ajouter_imprimante(nouvelle_imprimante)

    elif choix == 2:
        mon_atelier.afficher_tous()
        numero_serie = input("Entré le numéro de série de l'imprimante à retirer : ")
        mon_atelier.retirer_imprimante(numero_serie)

    elif choix == 3:
        mon_atelier.afficher_tous()

    elif choix == 4:
        choix_marque = input("Quel marque recherchez vous ? ")
        resultat = mon_atelier.chercher_par_marque(choix_marque)

    elif choix == 5:
        nombre = mon_atelier.imprimante_dispo()
        print(f"Le nombre d'imprimante dispo est : {nombre}")

    elif choix == 0:
        break
