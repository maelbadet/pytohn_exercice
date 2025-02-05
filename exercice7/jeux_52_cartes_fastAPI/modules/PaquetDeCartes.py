import random
from .Carte import Carte


class PaquetDeCartes:
	def __init__(self):
		"""Initialisation d'un paquet de cartes vide"""
		self.cartes = []  # Liste qui contiendra toutes les cartes
		self.couleurs = ["Trèfles", "Carreaux", "Cœurs", "Piques"]
		self.valeurs = [
			"As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
			"Valet", "Dame", "Roi"
		]

	def generer_paquet(self):
		"""Génère un paquet de 52 cartes"""
		self.cartes = [
			Carte(valeur, couleur) for couleur in self.couleurs for valeur in self.valeurs
		]

	def afficher_paquet(self):
		"""Affiche toutes les cartes dans le paquet"""
		for carte in self.cartes:
			print(carte)

	def melanger_paquet(self):
		"""Mélange les cartes du paquet"""
		random.shuffle(self.cartes)
