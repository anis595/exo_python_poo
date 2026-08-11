from classes.Livre import Livre


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres: list[Livre] = []

    def ajouter_livre(self, livre: Livre):
        """Cette méthode sert à ajouter un livre"""
        self.livres.append(livre)

    def retirer_livre(self, titre):
        """Cette méthode sert à supprimer un livre"""
        self.livres.remove(titre)

    def afficher_tous(self):
        for livre in self.livres:
            print(livre.afficher())

    def chercher_par_auteur(self, auteur):
        livres_trouves = []
        for livre in self.livres:
            if livre.auteur == auteur:
                livres_trouves.append(livre)
        return livres_trouves

    def nombre_dispo(self):
        compteur = 0
        for livre in self.livres:
            if livre.dispo:
                compteur += 1
        return compteur
