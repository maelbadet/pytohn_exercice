from question1.PaquetDeCartes import PaquetDeCartes
from question1.Carte import Carte

# Test 1 : verification de la bonne initialisation du paquet vide
paquet = PaquetDeCartes()
assert len(paquet.cartes) == 0, "Le paquet doit être vide après l'initialisation."

# Test 2 : verification de la bonne génération d'un paquet de 52 cartes
paquet.generer_paquet()
assert len(paquet.cartes) == 52, "Le paquet doit contenir 52 cartes après la génération."
cartes_attendues = [
	Carte(valeur, couleur) for couleur in paquet.couleurs for valeur in paquet.valeurs
]
assert all(carte in paquet.cartes for carte in cartes_attendues), "Toutes les cartes attendues doivent être présentes."

# Test 3 : verification du melange du paquet
cartes_avant_melange = list(paquet.cartes)
paquet.melanger_paquet()
assert cartes_avant_melange != paquet.cartes, "Le paquet mélangé doit avoir un ordre différent."
assert sorted(paquet.cartes, key=lambda c: (c.couleur, c.valeur)) == sorted(cartes_avant_melange,
                                                                            key=lambda c: (c.couleur, c.valeur)), \
	"Le paquet mélangé doit contenir exactement les mêmes cartes sans perte ni ajout."

# Test 4 : verification de l'affichage
try:
	paquet.afficher_paquet()
	print("Affichage des cartes exécuté avec succès.")
except Exception as e:
	assert False, f"La méthode afficher_paquet a levé une exception : {e}"
