from classes.Drone import Drone


class Flotte:
    def __init__(self, nom_equipe: str):
        self.nom_equipe = nom_equipe
        self.drones: list[Drone] = []

    def ajouter_drone(self, nouveau_drone):
        self.drones.append(nouveau_drone)

    def retirer_drone(self, numero_serie):
        for drone in self.drones:
            numero_serie = int(input("Saisissez le numéro de série"))
            if numero_serie == self.numero_serie:
                self.drones.remove(drone)
            print("Le drone a été supprimé")

    def afficher_tous(self):
        for drone in self.drones:
            drone.afficher()

    def chercher_par_marque(self, marque):
        list_drones = []
        for drone in self.drones:
            if drone.marque == marque:
                list_drones.append(drone)
            return list_drones

    def nombre_au_sol(self):
        count = 0
        for drone in self.drones:
            if drone.au_sol:
                count += 1

        return count
