from fastapi import FastAPI, HTTPException
from modules.Distribution import Distribution
from modules.PaquetDeCartes import PaquetDeCartes

# appel de FastAPI
app = FastAPI()


@app.get("/")
async def read_root():
	return {"message": "Bienvenue sur mon backend FastAPI!"}

@app.get("/cartes/")
def get_paquet_cartes():
	"""
    Endpoint pour récupérer un paquet de 52 cartes non mélangé.
    """
	paquet = PaquetDeCartes()
	paquet.generer_paquet()  # Générer un paquet de 52 cartes
	return {"paquet_de_cartes": [str(carte) for carte in paquet.cartes]}


@app.get("/cartes/melangees/")
def get_paquet_cartes_melangees():
	"""
       Endpoint pour récupérer un paquet de 52 cartes mélangé.
       """
	paquet = PaquetDeCartes()
	paquet.generer_paquet()
	paquet.melanger_paquet()
	return {"paquet_de_cartes": [str(carte) for carte in paquet.cartes]}


@app.get("/cartes/distribution/")
def get_paquets_pour_joueurs(nb_joueurs: int):
	"""
    Endpoint pour distribuer des cartes entre X joueurs.
    """
	# Vérification de la validité du nombre de joueurs
	if nb_joueurs <= 0:
		raise HTTPException(status_code=400, detail="Le nombre de joueurs doit être un entier positif.")

	paquet = PaquetDeCartes()
	paquet.generer_paquet()  # Générer un paquet de 52 cartes
	paquet.melanger_paquet()  # Mélanger le paquet

	try:
		# Distribution des cartes
		distribution = Distribution(paquet, nb_joueurs)
		distribution.distribuer()

		# Préparer le résultat
		result = {
			f"Joueur {i + 1}": [str(carte) for carte in main]
			for i, main in enumerate(distribution.mains)
		}
		if distribution.cartes_restantes:
			result["Cartes restantes"] = [str(carte) for carte in distribution.cartes_restantes]

		return result

	except ValueError as e:
		# Gérer l'erreur si trop de joueurs
		raise HTTPException(status_code=400, detail=str(e))
