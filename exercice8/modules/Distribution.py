from pprint import pprint


class Distribution:
	def __init__(self, paquet, nb_joueurs):
		"""
        Classe pour distribuer les cartes.
        :param paquet: PaquetDeCartes (le paquet mélangé à distribuer).
        :param nb_joueurs: int (nombre de joueurs).
        """
		self.paquet = paquet
		self.nb_joueurs = nb_joueurs
		self.mains = []  # Liste de mains, une pour chaque joueur
		self.cartes_restantes = []  # Liste des cartes inutilisées

	def distribuer(self):
		"""
        Distribution des cartes équitablement aux joueurs.
        Gère le cas où le nombre de cartes n'est pas divisible par le nombre de joueurs.
        """
		# Vérifier qu'il y a suffisamment de cartes pour tous les joueurs
		if self.nb_joueurs > len(self.paquet.cartes):
			raise ValueError("Le nombre de joueurs dépasse le nombre de cartes disponibles.")

		# creer une liste de joueurs vide, le '_' singifie, pas besoin de cette valeur
		self.mains = [[] for _ in range(self.nb_joueurs)]

		# Distribution des cartes
		for i, carte in enumerate(self.paquet.cartes):
			# Détermine à quel joueur attribuer la carte (ex: 1 % 5 = 1 donc carte attribuer au joueur 1)
			joueur = i % self.nb_joueurs #nb_joueur represente le nombre de joueur
			self.mains[joueur].append(carte)

		# Cartes restantes non distribuées (si div. non entière)
		total_cartes_distribuées = self.nb_joueurs * (len(self.paquet.cartes) // self.nb_joueurs)
		self.cartes_restantes = self.paquet.cartes[total_cartes_distribuées:]

	def afficher_mains(self):
		"""
        Affiche les cartes de chaque joueur ainsi que les cartes restantes si il y en a
        """
		result = {}  # Utiliser un dictionnaire pour relier les joueurs à leurs cartes
		for i, main in enumerate(self.mains):
			result[f"Joueur {i + 1}"] = [str(carte) for carte in main]
		pprint(result)

		# Afficher les cartes restantes, s'il y en a
		if self.cartes_restantes:
			print("\nCartes restantes :")
			for i, carte in enumerate(self.cartes_restantes, start=1):
				print(f"  Carte {i}: {carte}")
