import csv
import os
import pathlib


# Fonction pour exporter un dictionnaire dans un fichier CSV
def exporter_dictionnaire_vers_csv(dictionnaire, chemin_fichier_csv):
	try:
		# Création du dossier s'il n'existe pas
		dossier_csv = os.path.dirname(chemin_fichier_csv)
		os.makedirs(dossier_csv, exist_ok=True)

		with open(chemin_fichier_csv, 'w', encoding='utf-8', newline='') as fichier_csv:
			ecrivain = csv.writer(fichier_csv)

			# Écrire les noms des colonnes
			ecrivain.writerow(["Numéro de ligne", "Contenu"])

			# Écrire les lignes du dictionnaire
			for numero, contenu in dictionnaire.items():
				ecrivain.writerow([numero, contenu])

		print(f"Le fichier CSV a été généré avec succès : {chemin_fichier_csv}")
	except Exception as e:
		print(f"Une erreur est survenue lors de l'exportation vers CSV : {e}")


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


# Obtenir le chemin de la racine du projet
root_file = pathlib.Path(__file__).parent.parent.resolve()

# Chemin pour le fichier texte
chemin_texte = os.path.join(root_file, "exercice2", "test.txt")  # Exemple : un dossier "text_files"

# Chemin pour le fichier CSV à générer
chemin_csv = os.path.join(root_file, "exercice3/csv_files", "resultat.csv")  # Exemple : un dossier "csv_files"

# Convertir le fichier texte en dictionnaire
dictionnaire = fichier_vers_dictionnaire(chemin_texte)

# Exporter le dictionnaire dans un fichier CSV
if dictionnaire:  # Vérification si le dictionnaire n'est pas vide ou None
	exporter_dictionnaire_vers_csv(dictionnaire, chemin_csv)
