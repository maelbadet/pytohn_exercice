from fastapi import FastAPI

# Initialisation de l'application FastAPI
app = FastAPI()

# Liste d'items fictifs (base de données simulée)
ITEMS = [
	{"id": 1, "name": "Item A", "description": "Description de l'Item A"},
	{"id": 2, "name": "Item B", "description": "Description de l'Item B"},
	{"id": 3, "name": "Item C", "description": "Description de l'Item C"},
	{"id": 4, "name": "Item D", "description": "Description de l'Item D"},
	{"id": 5, "name": "Item E", "description": "Description de l'Item E"},
]

# Endpoint pour la page d'accueil
@app.get("/")
async def read_root():
	return {"message": "Bienvenue sur mon backend FastAPI!"}

@app.get("/items/")
async def get_items():
	"""
    Retourne la liste complète des items.
    """
	return {"items": ITEMS}


# Endpoint pour récupérer un item spécifique par son ID
@app.get("/items/{item_id}")
async def get_item(item_id: int):
	"""
    Retourne un item spécifique identifié par son ID.
    """
	# Recherche de l'item dans la liste
	for item in ITEMS:
		if item["id"] == item_id:
			return item

	# Si l'item n'est pas trouvé, lever une exception 404
	raise HTTPException(status_code=404, detail="Item non trouvé")

