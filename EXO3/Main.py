from classes.Drone import Drone
from classes.Flotte import Flotte


ma_flotte = Flotte("Ma flotte")

drone1 = Drone(1234, "5pouce", "Apex", 2020, True)
drone2 = Drone(3625, "6pouce", "Nazgul", 2023, True)
drone3 = Drone(3937, "7pouce", "Apex", 2027, False)

ma_flotte.ajouter_drone(drone3)


while True:
    print("1. Afficher tout les drones\n2. Ajouter un drone\n3. QUITTER ")
    choix = int(input("Quel est votre choix ?"))
    if choix == 1:
        ma_flotte.afficher_tous()
    elif choix == 2:
        num = input("Quel est le numéro de série ?")
        model = input("Quel est le model ? ")
        marque = input("Quel est la marque ? ")
        annee = int(input("Quel est l'année? "))
        nouveau_drone = Drone(num, model, marque, annee)
        ma_flotte.ajouter_drone(nouveau_drone)
    elif choix == 3:
        print("Extinction")
        break
