from exercice5.modules import PaquetDeCartes
from exercice5.modules import Distribution
from pprint import pprint


def main():
	# Créer un paquet de cartes
	paquet = PaquetDeCartes()

	# Générer et mélanger le paquet
	paquet.generer_paquet()
	paquet.melanger_paquet()

	# Demander le nombre de joueurs
	while True:
		try:
			nb_joueurs = int(input("Entrez le nombre de joueurs : "))
			if nb_joueurs <= 0:
				print("Le nombre de joueurs doit être un entier positif.")
				continue
			break
		except ValueError:
			print("Veuillez entrer un nombre entier.")
	#distribution des cartes si n <= 52
	try:
		distribution = Distribution(paquet, nb_joueurs)
		distribution.distribuer()

		# Afficher les mains des joueurs
		print("\nCartes distribuées :\n")
		distribution.afficher_mains()
	except ValueError as e:
		# Gérer l'erreur si les joueurs > nombre de cartes
		print(f"\nErreur : {e}")


if __name__ == "__main__":
	main()
