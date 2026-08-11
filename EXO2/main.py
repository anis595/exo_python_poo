from classes.Livre import Livre
from classes.Bibliotheque import Bibliotheque

livre1 = Livre(12, "cl", "cl", 2021, True)
livre2 = Livre(13, "cla", "clo", 2022, True)
livre3 = Livre(14, "clau", "cloc", 2023, True)
livre4 = Livre(15, "claud", "clocl", 2024, True)

# livre1.afficher()


biblio = Bibliotheque("mabiblio")

# biblio.ajouter_livre(livre3)
# biblio.afficher_tous(livre3, livre2)
Livre.emprunter(livre2)
