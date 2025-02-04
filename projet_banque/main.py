from bank import IdentiteClient, CompteBancaire, CompteParticulier


def main():
	# Création de l'identité d'un client
	client1 = IdentiteClient(nom="Dupont", prenom="Alice", adresse="5 Rue des Lilas")
	print(f"Client créé : {client1}")

	# Création d'un compte bancaire standard
	compte_bancaire = CompteBancaire(identite=client1, solde=1000.0)
	print("\n=== Compte Bancaire Standard ===")
	compte_bancaire.afficher_solde()
	compte_bancaire.deposer(500)
	compte_bancaire.retirer(300)
	compte_bancaire.afficher_solde()

	# Création d'un compte bancaire pour un particulier avec découvert autorisé
	client2 = IdentiteClient(nom="Martin", prenom="Paul", adresse="24 Avenue des Champs")
	compte_particulier = CompteParticulier(identite=client2, solde=200.0, decouvert_autorise=300.0)

	print("\n=== Compte Bancaire Particulier ===")
	compte_particulier.afficher_solde()
	compte_particulier.deposer(100)
	compte_particulier.retirer(500)  # Autorisé grâce au découvert
	compte_particulier.afficher_solde()
	compte_particulier.retirer(200)  # Dépassement non autorisé
	compte_particulier.afficher_solde()


if __name__ == "__main__":
	main()
