class IdentiteClient:
	"""Classe représentant l'identité d'un client."""

	def __init__(self, nom: str, prenom: str, adresse: str):
		self.nom = nom
		self.prenom = prenom
		self.adresse = adresse

	def __str__(self):
		return f"{self.prenom} {self.nom}, Adresse: {self.adresse}"
