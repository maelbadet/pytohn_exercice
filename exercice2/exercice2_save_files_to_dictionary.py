import pathlib


def fichier_vers_dictionnaire(chemin_fichier):
	contenu_dictionnaire = {}
	try:
		with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
			for numero, ligne in enumerate(fichier, start=1):
				contenu_dictionnaire[numero] = ligne.strip()  # Numéro de la ligne comme clé
		return contenu_dictionnaire
	except FileNotFoundError:
		print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
	except Exception as e:
		print(f"Une erreur inattendue est survenue : {e}")
		return None


# Exemple d’affichage en fonction des lignes du dictionnaire
def afficher_contenu_dictionnaire(contenu_dictionnaire):
	if not contenu_dictionnaire:
		print("Le dictionnaire est vide ou non valide.")
		return

	for numero, contenu in contenu_dictionnaire.items():
		print(f"Ligne numéro {numero} : {len(contenu)} caractères → « {contenu} »")


# Obtenir le chemin du fichier root a la racine de l'exercice
root_path = pathlib.Path(__file__).parent.resolve()
chemin_exemple = root_path / "test.txt"

# Exemple d'appel
dictionnaire = fichier_vers_dictionnaire(chemin_exemple)
afficher_contenu_dictionnaire(dictionnaire)
