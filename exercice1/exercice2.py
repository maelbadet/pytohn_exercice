def valider_ipv4(adresse_ipv4):
	"""
	Vérifie si une adresse IPv4 est valide.
	:param adresse_ipv4: Adresse IPv4 sous forme de chaîne (exemple : '192.168.0.1')
	:return: True si l'adresse est valide, sinon déclenche une exception ValueError.
	"""
	# Diviser l'adresse en octets
	octets = adresse_ipv4.split(".")

	# Vérification si l'adresse contient exactement 4 octets
	if len(octets) != 4:
		raise ValueError("L'adresse IPv4 doit contenir exactement 4 octets.")

	# Vérifier que chaque octet est un entier compris entre 0 et 255
	for i, octet in enumerate(octets):
		if not octet.isdigit():
			raise ValueError(f"Octet {i + 1} ('{octet}') n'est pas un entier valide.")

		valeur = int(octet)
		if valeur < 0 or valeur > 255:
			raise ValueError(f"Octet {i + 1} ('{valeur}') doit être entre 0 et 255.")

	return True  # L'adresse est valide.


def main():
	print("Bienvenue dans l'application de validation des adresses IP !")

	# Entré utilisateur
	adresse_ip = input("Veuillez entrer une adresse IP (IPv4) : ").strip()

	try:
		# Vérification de l'adresse IPv4 (on peut ajouter IPv6 ensuite)
		if "." in adresse_ip:
			valider_ipv4(adresse_ip)
			print(f"L'adresse IPv4 {adresse_ip} est valide.")

	except ValueError as e:
		print(f"Erreur : {e}. Veuillez entrer une adresse IP valide.")


if __name__ == "__main__":
	main()
