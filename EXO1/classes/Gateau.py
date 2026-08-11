class Gateau:
    def __init__(self, nom_gateau, temps, liste, etapes, createur):
        self.nom_gateau = nom_gateau
        self.temps = temps
        self.liste = liste
        self.etapes = etapes
        self.createur = createur

    def afficher(self):
        print("Nom du gateau : ", self.nom_gateau)
        print("Temps : ", self.temps)
        print("Liste : ", self.liste)
        print("Etapes : ", self.etapes)
        print("Createur : ", self.createur)

    def afficher_ingredient(self):
        print("Liste des ingredients : ", self.liste)
