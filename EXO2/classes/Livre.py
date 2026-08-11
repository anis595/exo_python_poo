class Livre:
    def __init__(self, isbn, titre, auteur, annee, dispo=True):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.dispo = True

    def emprunter(self):
        if self.dispo:
            self.dispo = False
        else:
            print(f"{self.titre} est déjà emprunter")

    def retourner(self):
        self.dispo == True

    def afficher(self):
        statut = "Disponible" if self.dispo else "Emprunté"
        return f"{self.titre} de {self.auteur} ({self.annee}) - {statut}"
