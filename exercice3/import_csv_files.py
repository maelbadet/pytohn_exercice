import csv


# Fonction pour lire un fichier CSV
def lire_fichier_csv(chemin_fichier):
	donnees = []
	with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
		lecteur_csv = csv.reader(fichier)
		en_tetes = next(lecteur_csv)  # Lire les en-têtes
		for ligne in lecteur_csv:
			donnees.append(ligne)
	return en_tetes, donnees


# Fonction pour modifier les données
def modifier_contenu(donnees):
	donnees_modifiees = []
	for ligne in donnees:
		# Exemple : on incrémente une valeur numérique dans la 1ère colonne
		nouvelle_ligne = [int(ligne[0]) + 1 if ligne[0].isdigit() else ligne[0]] + ligne[1:]
		donnees_modifiees.append(nouvelle_ligne)
	return donnees_modifiees


# Fonction pour sauvegarder les données modifiées dans un fichier CSV
def sauvegarder_csv(chemin_fichier, en_tetes, donnees):
	with open(chemin_fichier, mode='w', encoding='utf-8', newline='') as fichier:
		ecrivain_csv = csv.writer(fichier)
		ecrivain_csv.writerow(en_tetes)  # Écrire les en-têtes
		ecrivain_csv.writerows(donnees)  # Écrire les données


# Chemins des fichiers CSV
fichier_original = "fichier_original.csv"
fichier_modifie = "fichier_modifie.csv"

# Étapes de traitement
en_tetes, donnees = lire_fichier_csv(fichier_original)  # Étape 1 : Lecture
donnees_modifiees = modifier_contenu(donnees)  # Étape 2 : Modification
sauvegarder_csv(fichier_modifie, en_tetes, donnees_modifiees)  # Étape 3 : Sauvegarde

print("Le fichier CSV modifié a été sauvegardé dans :", fichier_modifie)
