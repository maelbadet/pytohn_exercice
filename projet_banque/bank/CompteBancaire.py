from projet_banque.bank import IdentiteClient


class CompteBancaire:
	"""Classe représentant un compte bancaire générique."""

	def __init__(self, identite: IdentiteClient, solde: float = 0.0):
		self.identite = identite
		self.solde = solde

	def deposer(self, montant: float):
		"""Ajoute un montant au solde du compte."""
		if montant > 0:
			self.solde += montant
			print(f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€.")
		else:
			print("Le montant à déposer doit être positif.")

	def retirer(self, montant: float):
		"""Retire un montant du solde du compte."""
		if 0 < montant <= self.solde:
			self.solde -= montant
			print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€.")
		else:
			print("Montant invalide ou solde insuffisant.")

	def afficher_solde(self):
		"""Affiche le solde actuel du compte."""
		print(f"Le solde actuel du compte est : {self.solde}€.")
