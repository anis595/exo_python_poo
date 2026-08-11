from classes.Livre import Livre
from classes.Bibliotheque import Bibliotheque

livre1 = Livre(12, "cl", "cl", 2021, True)
livre2 = Livre(13, "cla", "clo", 2022, True)
livre3 = Livre(14, "clau", "cloc", 2023, True)
livre4 = Livre(15, "claud", "clocl", 2024, True)

# livre1.afficher()


biblio = Bibliotheque("mabiblio")

biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.ajouter_livre(livre3)
biblio.ajouter_livre(livre4)

livre1.emprunter()
livre1.emprunter()
livre1.retourner()
print(livre1.afficher())
biblio.afficher_tous()
print(f"Livres disponibles : {biblio.nombre_dispo()}")
livres_auteur = biblio.chercher_par_auteur("Auteur1")

for livre in livres_auteur:
    print(livre.afficher())

biblio.retirer_livre("Livre1")
