# main.py

from module1.ip_operations import IPv4Validator


def main():
	print("Bienvenue dans l'application de validation et traitement d'IPv4 !")

	# Créer une instance de la classe
	ipv4_validator = IPv4Validator()

	while True:
		print("\nOptions :")
		print("1 - Définir une adresse IPv4")
		print("2 - Afficher l'adresse IPv4 actuelle")
		print("3 - Valider l'adresse IPv4 actuelle")
		print("4 - Quitter")
		choix = input("Veuillez sélectionner une option (1, 2, 3, 4) : ").strip()

		if choix == "1":
			adresse = input("Veuillez entrer une adresse IPv4 : ").strip()
			ipv4_validator.definir_adresse(adresse)
			print("Adresse définie avec succès.")
		elif choix == "2":
			ipv4_validator.afficher_adresse()
		elif choix == "3":
			try:
				if ipv4_validator.valider_adresse():
					print("L'adresse IPv4 est valide.")
			except ValueError as e:
				print(f"Erreur : {e}")
		elif choix == "4":
			print("Au revoir !")
			break
		else:
			print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
	main()
