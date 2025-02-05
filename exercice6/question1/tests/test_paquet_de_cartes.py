from question1.PaquetDeCartes import PaquetDeCartes
from question1.Carte import Carte


def test_initialisation_paquet_vide():
	"""Vérifie que le paquet est vide après initialisation."""
	paquet = PaquetDeCartes()
	assert len(paquet.cartes) == 0, "Le paquet doit être initialisé vide."


def test_generer_paquet():
	"""Vérifie que la méthode génère un paquet complet de 52 cartes."""
	paquet = PaquetDeCartes()
	paquet.generer_paquet()

	assert len(paquet.cartes) == 52, "Le paquet généré doit contenir 52 cartes."

	cartes_attendues = [
		Carte(valeur, couleur) for couleur in paquet.couleurs for valeur in paquet.valeurs
	]

	# Vérifie que toutes les cartes attendues sont présentes
	for carte in cartes_attendues:
		assert carte in paquet.cartes, f"La carte {carte} doit être présente dans le paquet."


def test_melanger_paquet():
	"""Vérifie que le paquet est mélangé correctement."""
	paquet = PaquetDeCartes()
	paquet.generer_paquet()

	cartes_avant_melange = list(paquet.cartes)  # Copie de l'état avant mélange
	paquet.melanger_paquet()

	# Vérifie que l'ordre est différent après le mélange
	assert cartes_avant_melange != paquet.cartes, "Le paquet mélangé doit avoir un ordre différent."

	# Vérifie qu'aucune carte n'a été perdue ou ajoutée
	assert sorted(paquet.cartes, key=lambda c: (c.couleur, c.valeur)) == sorted(cartes_avant_melange,
	                                                                            key=lambda c: (c.couleur, c.valeur)), \
		"Le contenu du paquet mélangé doit être identique à celui du paquet non mélangé."


def test_afficher_paquet(capsys):
	"""Vérifie que la méthode afficher_paquet affiche 52 cartes."""
	paquet = PaquetDeCartes()
	paquet.generer_paquet()

	paquet.afficher_paquet()

	# Capture la sortie du print
	captured = capsys.readouterr()
	sorties = captured.out.strip().split("\n")

	assert len(sorties) == 52, "La méthode afficher_paquet doit afficher 52 cartes."
