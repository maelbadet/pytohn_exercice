import fileinput


def remplacer_lettres_par_x(chemin_fichier, lettres_a_remplacer):
	try:
		with fileinput.FileInput(chemin_fichier, inplace=True, backup=".bak") as fichier:
			for ligne in fichier:
				for lettre in lettres_a_remplacer:
					ligne = ligne.replace(lettre, "x")  # Remplace les lettres spécifiées
				print(ligne, end='')  # Réécrit dans le fichier
		print(f"Remplacement effectué avec succès dans '{chemin_fichier}'.")
	except FileNotFoundError:
		print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
	except Exception as e:
		print(f"Une erreur inattendue est survenue : {e}")


# Exemple d'appel
chemin_exemple = "C:/Users/maelb/PycharmProjects/exercice2/test.txt"  # Remplacez avec le chemin de votre fichier
remplacer_lettres_par_x(chemin_exemple, lettres_a_remplacer=["a", "e", "i", "o", "u"])  # Remplace les voyelles
