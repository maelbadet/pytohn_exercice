import requests
import json


def fetch_fbi_api_data(endpoint: str, params: dict = None) -> dict:
	"""
    Méthode générique pour récupérer les données de l'API FBI Wanted.
    Gère les erreurs et retourne les données JSON.

    :param endpoint: (str) L'URL complète de l'API.
    :param params: (dict) Les paramètres de recherche GET.
    :return: (dict) Les données issues de l'API ou une erreur détaillée.
    """
	try:
		# Effectuer une requête GET
		response = requests.get(endpoint, params=params)

		# Vérifier les codes de statut HTTP
		response.raise_for_status()

		# Convertir et retourner le contenu JSON
		return json.loads(response.content)

	except requests.exceptions.HTTPError as http_err:
		print(f"Erreur HTTP: {http_err}")
		return {"error": f"HTTPError: {response.status_code}"}

	except requests.RequestException as req_err:
		print(f"Erreur de requête: {req_err}")
		return {"error": "Une erreur réseau s'est produite."}

if __name__ == "__main__":
	url = "https://api.fbi.gov/wanted/v1/list"

	# Utilisation de la pagination
	data = fetch_fbi_api_data(url, params={"page": 2})
	if "error" not in data:
		print(f"Numéro de page : {data['page']}")
		print(f"Premier élément : {data['items'][0]['title']}")
		print(f"Deuxieme élément : {data['items'][1]['title']}")
		print(f"Troisieme élément : {data['items'][2]['title']}")
	else:
		print(data['error'])
