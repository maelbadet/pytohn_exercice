class Carte:
	def __init__(self, valeur, couleur):
		self.valeur = valeur
		self.couleur = couleur

	# faire la comparaison d'equivalence dans les tests unitaires
	def __eq__(self, other):
		if isinstance(other, Carte):
			return self.valeur == other.valeur and self.couleur == other.couleur
		return False

	# Pour utiliser des objets Carte dans des conteneurs comme 'in'
	def __hash__(self):
		return hash((self.valeur, self.couleur))

	# methode pour faciliter le débogage
	def __repr__(self):
		return f"{self.valeur} de {self.couleur}"
