from classes.Imprimante3D import Imprimante3D


class Atelier3D:
    def __init__(self, nom: str):
        self.nom = nom
        self.imprimantes: list[Imprimante3D] = []

    def ajouter_imprimante(self, imprimante):
        # for imprimante in self.imprimantes:
        self.imprimantes.append(imprimante)

    def retirer_imprimante(self, numero_serie):
        for imprimante in self.imprimantes:
            if numero_serie == imprimante.numero_serie:
                self.imprimantes.remove(imprimante)
                break

    def afficher_tous(self):
        for imprimante in self.imprimantes:
            imprimante.afficher()

    def chercher_par_marque(self, marque):
        list_imprimante = []
        for imprimante in self.imprimantes:
            if marque == imprimante.marque:
                list_imprimante.append(imprimante)
        return list_imprimante

    def imprimante_dispo(self):
        count = 0
        for imprimante in self.imprimantes:
            if imprimante.dispo == True:
                count += 1
        return count
