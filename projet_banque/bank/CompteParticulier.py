from projet_banque.bank import CompteBancaire, IdentiteClient


class CompteParticulier(CompteBancaire):
	"""Classe représentant un compte bancaire pour un particulier."""

	def __init__(self, identite: IdentiteClient, solde: float = 0.0, decouvert_autorise: float = 0.0):
		super().__init__(identite, solde)
		self.decouvert_autorise = decouvert_autorise

	def retirer(self, montant: float):
		"""Permet un retrait même avec un découvert autorisé."""
		if 0 < montant <= (self.solde + self.decouvert_autorise):
			self.solde -= montant
			print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€.")
		else:
			print("Montant invalide ou dépassement de découvert autorisé.")
