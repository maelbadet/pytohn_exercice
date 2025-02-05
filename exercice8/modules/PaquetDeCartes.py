import random
from .Carte import Carte
from db import *
from models import *


class PaquetDeCartes:
	def __init__(self):
		"""Initialisation d'un paquet de cartes vide"""
		self.cartes = []  # Liste qui contiendra toutes les cartes
		self.couleurs = ["Trèfles", "Carreaux", "Cœurs", "Piques"]
		self.valeurs = [
			"As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
			"Valet", "Dame", "Roi"
		]

	async def generer_paquet(self):
		"""Génère un paquet de 52 cartes et les stocke dans la base de données"""
		try:
			# Création d'un paquet de cartes
			print("Début de la génération du paquet de cartes...")
			self.cartes = [
				Carte(valeur, couleur) for couleur in self.couleurs for valeur in self.valeurs
			]

			print(f"{len(self.cartes)} cartes générées avec succès.")

			# Insérer les cartes dans la base de données
			if not database.is_connected:
				raise RuntimeError("La base de données n'est pas connectée.")

			query = cartes_table.insert()
			values = [{"valeur": carte.valeur, "couleur": carte.couleur} for carte in self.cartes]

			print("Données d'insertion : ", values[:5])  # Vérifier un échantillon des données

			await database.execute_many(query, values)

			print("Insertion des cartes en base réussie.")
		except Exception as e:
			print(f"Erreur lors de la génération du paquet : {e}")
			raise

	def afficher_paquet(self):
		"""Affiche toutes les cartes dans le paquet"""
		for carte in self.cartes:
			print(carte)

	def melanger_paquet(self):
		"""Mélange les cartes du paquet"""
		random.shuffle(self.cartes)
