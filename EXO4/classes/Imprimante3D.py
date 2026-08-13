class Imprimante3D:
    def __init__(
        self, numero_serie: str, model: str, marque: str, annee: int, dispo=True
    ):
        self.numero_serie = numero_serie
        self.model = model
        self.marque = marque
        self.annee = annee
        self.dispo = dispo

    def lancer_impression(self):
        if self.dispo == True:
            self.dispo == False

        else:
            print("Imprimante indisponible")

    def terminer_impression(self):
        if self.dispo == False:
            self.dispo == True

    def afficher(self):
        print(
            f'Le numéro de série est : {self.numero_serie}\nLe modéle est : {self.model}\nLa marque est : {self.marque}\n L"année est : {self.annee}\n Dispo :{self.dispo}'
        )
