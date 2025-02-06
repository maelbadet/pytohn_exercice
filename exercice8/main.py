import random

from fastapi import FastAPI, HTTPException
from db import database, init_db
from modules import PaquetDeCartes, Distribution
from models import cartes_table, joueurs_table, distribution_table

app = FastAPI()


@app.on_event("startup")
async def startup():
	await database.connect()
	await init_db()  # Création des tables


@app.on_event("shutdown")
async def shutdown():
	await database.disconnect()


# appel de fastAPI avec base de donnee


@app.get("/")
async def read_root():
	return {"message": "Bienvenue sur mon backend FastAPI!"}


@app.post("/cartes/init/")
async def ajouter_cartes_a_la_bdd():
	"""
    Endpoint pour ajouter les 52 cartes dans la base de données.
    """
	try:
		if not database.is_connected:
			raise HTTPException(status_code=500, detail="La base de données n'est pas connectée.")

		# Vérifiez si les cartes existent déjà dans la DB
		query = cartes_table.select()
		cartes_existantes = await database.fetch_all(query)

		if cartes_existantes:
			raise HTTPException(status_code=400, detail="Le paquet de cartes existe déjà dans la base de données.")

		# Création du paquet de 52 cartes
		paquet = PaquetDeCartes()
		await paquet.generer_paquet()

		return {"message": "Les cartes ont été ajoutées à la base de données avec succès."}
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Une erreur est survenue : {str(e)}")


@app.get("/cartes/")
async def recuperer_cartes():
	"""
         Endpoint pour récupérer toutes les cartes de la base de données.
         """
	query = cartes_table.select()
	cartes = await database.fetch_all(query)
	return [{"id": carte.id, "valeur": carte.valeur, "couleur": carte.couleur} for carte in cartes]


@app.get("/cartes/melangees/")
async def distribuer_paquet(nb_joueurs: int):
	"""
    Endpoint pour mélanger les cartes et les distribuer à un nombre donné de joueurs.
    """
	if nb_joueurs <= 0:
		raise HTTPException(status_code=400, detail="Le nombre de joueurs doit être un entier positif.")

	try:
		# Vérification de la connexion à la base de données
		if not database.is_connected:
			raise HTTPException(status_code=500, detail="La base de données n'est pas connectée.")

		# Charger toutes les cartes à partir de la base de données
		query = cartes_table.select()
		cartes = await database.fetch_all(query)

		if not cartes:
			raise HTTPException(status_code=400, detail="Aucune carte n'a été trouvée dans la base de données.")

		cartes_list = [dict(carte) for carte in cartes]
		random.shuffle(cartes_list)

		# Diviser les cartes entre les joueurs
		nb_cartes_par_joueur = len(cartes_list) // nb_joueurs
		mains = [
			cartes_list[i * nb_cartes_par_joueur: (i + 1) * nb_cartes_par_joueur]
			for i in range(nb_joueurs)
		]

		cartes_restantes = cartes_list[nb_joueurs * nb_cartes_par_joueur:]

		# Sauvegarder les joueurs dans la base de données
		joueurs = [{"nom": f"Joueur {i + 1}"} for i in range(nb_joueurs)]
		joueur_ids = []
		for joueur in joueurs:
			joueur_id = await database.execute(joueurs_table.insert().values(joueur))
			joueur_ids.append(joueur_id)

		# Sauvegarder la distribution des cartes
		for i, main in enumerate(mains):
			joueur_id = joueur_ids[i]
			distributions = [{"joueur_id": joueur_id, "carte_id": carte["id"]} for carte in main]
			await database.execute_many(distribution_table.insert(), distributions)

		return {
			"message": "Cartes mélangées et distribuées avec succès.",
			"distribution": {
				f"Joueur {i + 1}": [{"valeur": carte['valeur'], "couleur": carte['couleur']} for carte in main]
				for i, main in enumerate(mains)
			},
			"cartes_restantes": [{"valeur": carte['valeur'], "couleur": carte['couleur']} for carte in
			                     cartes_restantes],
		}

	except Exception as e:
		print(f"Erreur lors de la distribution des cartes : {e}")
		raise HTTPException(status_code=500, detail=f"Une erreur est survenue : {str(e)}")


@app.get("/joueurs/")
async def recuperer_joueurs():
	"""
         Endpoint pour récupérer tous les joueurs de la base de données.
         """
	query = joueurs_table.select()
	joueurs = await database.fetch_all(query)
	return [{"id": joueur.id, "nom": joueur.nom} for joueur in joueurs]


@app.get("/distribution/")
async def recuperer_distribution():
	"""
         Endpoint pour récupérer toutes les distributions de cartes de la base de données.
         """
	query = distribution_table.select()
	distributions = await database.fetch_all(query)
	return [{"id": distribution.id, "id_joueur": distribution.joueur_id, "id_cartes": distribution.carte_id} for
	        distribution in distributions]
