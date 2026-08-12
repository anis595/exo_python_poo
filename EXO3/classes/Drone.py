class Drone:
    def __init__(self, numero_serie, model, marque, annee_achat, au_sol=True):
        self.numero_serie = numero_serie
        self.model = model
        self.marque = marque
        self.annee_achat = annee_achat
        self.au_sol = True

    def decoller(self):
        self.au_sol == False
        print(f"Le drone est dèjà en mission, {self.au_sol}")

    def atterrir(self):
        self.au_sol == True

    def afficher(self):
        print(
            f"Les caractéristiques du drone sont : \n Numéro de série : {self.numero_serie}\n Modéle : {self.model}\n Marque : {self.marque}\n L'année d'achat : {self.annee_achat}"
        )
