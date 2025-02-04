import os
import pathlib
import json


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


# Fonction pour exporter le dictionnaire dans un fichier JSON
def exporter_dictionnaire_vers_json(dictionnaire, chemin_fichier_json):
	try:
		# Création du dossier s'il n'existe pas
		dossier_json = os.path.dirname(chemin_fichier_json)
		os.makedirs(dossier_json, exist_ok=True)

		with open(chemin_fichier_json, 'w', encoding='utf-8') as fichier_json:
			json.dump(dictionnaire, fichier_json, indent=4, ensure_ascii=False)
		print(f"Le fichier JSON a été créé avec succès : {chemin_fichier_json}")
	except Exception as e:
		print(f"Une erreur est survenue lors de la création du fichier JSON : {e}")

# Obtenir le chemin racine du projet
root_file = pathlib.Path(__file__).parent.resolve()

# Chemin du fichier texte
chemin_texte = os.path.join(root_file, "text_files", "test.txt")  # Par exemple un répertoire 'text_files'

# Chemin du fichier JSON à générer
chemin_json = os.path.join(root_file, "json_files", "resultat.json")  # Par exemple un répertoire 'json_files'

# Convertir le fichier texte en dictionnaire
dictionnaire = fichier_vers_dictionnaire(chemin_texte)

# Exporter le dictionnaire dans un fichier JSON
if dictionnaire:  # Vérification si le dictionnaire n’est pas vide ou None
	exporter_dictionnaire_vers_json(dictionnaire, chemin_json)
