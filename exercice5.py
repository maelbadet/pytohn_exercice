def valider_liste_adresses_ip(adresses):
	"""
	Valide une liste d'adresses IP (IPv4 ou IPv6).
	:param adresses: Liste de chaînes représentant des adresses IP
	:return: Une liste d'adresses valides (avec leur type) et une liste d'erreurs pour les adresses invalides
	"""
	adresses_valides = []
	erreurs = []

	for adresse in adresses:
		try:
			type_ip = valider_adresse_ip(adresse)  # Utilise la méthode unifiée précédemment définie
			adresses_valides.append((adresse, type_ip))
		except ValueError as e:
			erreurs.append((adresse, str(e)))

	return adresses_valides, erreurs


def valider_dictionnaire_adresses_ip(dictionnaire_adresses):
	"""
	Valide un dictionnaire contenant des noms d'hôte et des adresses IP.
	:param dictionnaire_adresses: Un dictionnaire où les clés sont les noms d'hôte et les valeurs sont des adresses IP
	:return: Deux dictionnaires : un pour les adresses valides et un pour les adresses invalides
	"""
	adresses_valides = {}
	adresses_invalides = {}

	for host, adresse in dictionnaire_adresses.items():
		try:
			type_ip = valider_adresse_ip(adresse)  # Utilise la méthode unifiée précédemment définie
			adresses_valides[host] = (adresse, type_ip)  # Ajouter l'adresse valide avec son type (IPv4 ou IPv6)
		except ValueError as e:
			adresses_invalides[host] = (adresse, str(e))  # Ajouter l'adresse invalide avec l'erreur

	return adresses_valides, adresses_invalides


def valider_adresse_ip(adresse_ip):
	"""
	Valide une adresse IP (IPv4 ou IPv6).
	:param adresse_ip: Adresse IP sous forme de chaîne
	:return: 'IPv4' si l'adresse est une IPv4 valide, 'IPv6' si l'adresse est une IPv6 valide
			 Déclenche une exception ValueError si l'adresse IP est invalide
	"""
	# Détecter si c'est une adresse IPv4 (présence de ".")
	if "." in adresse_ip:
		# Validation IPv4
		octets = adresse_ip.split(".")
		if len(octets) != 4:
			raise ValueError("L'adresse IPv4 doit contenir exactement 4 octets.")

		for i, octet in enumerate(octets):
			if not octet.isdigit():
				raise ValueError(f"Octet {i + 1} ('{octet}') n'est pas un entier valide.")

			valeur = int(octet)
			if valeur < 0 or valeur > 255:
				raise ValueError(f"Octet {i + 1} ('{valeur}') doit être entre 0 et 255.")

		return "IPv4"
	elif ":" in adresse_ip:
		# Validation IPv6
		blocs = adresse_ip.split(":")

		if len(blocs) > 8:
			raise ValueError("L'adresse IPv6 ne peut pas contenir plus de 8 blocs.")

		if "" in blocs:
			# Vérifier la validité de "::"
			if adresse_ip.count("::") > 1:
				raise ValueError("L'adresse IPv6 ne peut contenir qu'un seul raccourci '::'.")
			elif adresse_ip == "::":
				return "IPv6"  # Cas spécial : l'adresse "::" est valide

			# Remplacer "::" par des blocs de zéros pour faciliter la vérification
			index_double_colon = blocs.index("")
			blocs.pop(index_double_colon)
			while len(blocs) < 8:
				blocs.insert(index_double_colon, "0")

		for i, bloc in enumerate(blocs):
			if bloc == "":
				continue  # Autoriser les blocs vides à cause de "::"
			if len(bloc) > 4:
				raise ValueError(f"Bloc {i + 1} ('{bloc}') contient plus de 4 caractères hexadécimaux.")
			try:
				# Les blocs doivent être valides en hexadécimal
				valeur = int(bloc, 16)
				if valeur < 0 or valeur > 0xFFFF:
					raise ValueError(f"Bloc {i + 1} ('{bloc}') doit être compris entre 0 et FFFF.")
			except ValueError:
				raise ValueError(f"Bloc {i + 1} ('{bloc}') n'est pas un nombre hexadécimal valide.")

		return "IPv6"

	# Si ce n'est ni IPv4 ni IPv6
	else:
		raise ValueError("Format d'adresse inconnu. Ce n'est ni une IPv4 ni une IPv6.")


def main():
	print("Bienvenue dans l'application de validation des adresses IP !")

	# Exemple 1 : Valider une liste d'adresses
	adresses_ip = [
		'192.168.0.1',  # IPv4 valide
		'256.100.50.25',  # IPv4 invalide (256 hors limite)
		'fe80::1ff:fe23:4567:890a',  # IPv6 valide
		'2001:db8::85a3::8a2e:370:7334',  # IPv6 invalide (deux "::")
		'abcd'  # Format inconnu
	]

	print("\nValidation d'une liste d'adresses IP...")
	valides, erreurs = valider_liste_adresses_ip(adresses_ip)
	print("\nAdresses IP valides :")
	for adresse, type_ip in valides:
		print(f"  - {adresse} ({type_ip})")

	print("\nAdresses IP invalides :")
	for adresse, erreur in erreurs:
		print(f"  - {adresse} (Erreur : {erreur})")

	# Exemple 2 : Valider un dictionnaire avec noms d'hôte et adresses IP
	dictionnaire_adresses = {
		'host1': '192.168.0.1',  # IPv4 valide
		'host2': '256.100.50.25',  # IPv4 invalide
		'host3': 'fe80::1ff:fe23:4567:890a',  # IPv6 valide
		'host4': '2001:db8::85a3::8a2e:370:7334',  # IPv6 invalide
		'host5': 'abcd'  # Format inconnu
	}

	print("\nValidation d'un dictionnaire d'hôtes et adresses IP...")
	valides, invalides = valider_dictionnaire_adresses_ip(dictionnaire_adresses)

	print("\nHôtes avec adresses IP valides :")
	for host, (adresse, type_ip) in valides.items():
		print(f"  - {host} : {adresse} ({type_ip})")

	print("\nHôtes avec adresses IP invalides :")
	for host, (adresse, erreur) in invalides.items():
		print(f"  - {host} : {adresse} (Erreur : {erreur})")


if __name__ == "__main__":
	main()
