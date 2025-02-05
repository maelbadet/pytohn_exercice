class Carte:
	def __init__(self, valeur, couleur):
		self.valeur = valeur
		self.couleur = couleur

	def __repr__(self):
		"""Représentation lisible d'une carte"""
		return f"{self.valeur} de {self.couleur}"
