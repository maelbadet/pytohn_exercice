def valider_adresse_ip(adresse_ip):
	"""
	Valide une adresse IP (IPv4 ou IPv6).
	:param adresse_ip: Adresse IP sous forme de chaîne
	:return: 'IPv4' si l'adresse est une IPv4 valide, 'IPv6' si l'adresse est une IPv6 valide
			 Déclenche une exception ValueError si l'adresse IP est invalide
	"""
	if "." in adresse_ip:  # Identifie une IPv4
		octets = adresse_ip.split(".")
		if len(octets) != 4:
			raise ValueError("L'adresse IPv4 doit contenir exactement 4 octets.")

		for i, octet in enumerate(octets):
			if not octet.isdigit() or not (0 <= int(octet) <= 255):
				raise ValueError(f"Octet {i + 1} ('{octet}') doit être entre 0 et 255.")

		# Détection des cas spécifiques pour IPv4
		premier_octet = int(octets[0])
		deuxieme_octet = int(octets[1])

		# une adresse privée commence toujours par 192.168.
		if premier_octet == 192 and deuxieme_octet == 168:
			return "IPv4 (Privée)"
		# une adresse locale est toujours 127.0.0.1.
		elif premier_octet == 127:
			return "IPv4 (local)"
		else:
			return "IPv4 (Publique)"


	elif ":" in adresse_ip:  # Identifie une IPv6
		blocs = adresse_ip.split(":")
		if len(blocs) > 8:
			raise ValueError("L'adresse IPv6 ne peut pas contenir plus de 8 blocs.")

		if "" in blocs:  # Gérer le raccourci "::"
			if adresse_ip.count("::") > 1:
				raise ValueError("L'adresse IPv6 ne peut contenir qu'un seul raccourci '::'.")
			blocs = [bloc for bloc in blocs if bloc != ""]
			while len(blocs) < 8:
				blocs.insert(blocs.index(""), "0")

		for i, bloc in enumerate(blocs):
			if not (0 <= int(bloc, 16) <= 0xFFFF):
				raise ValueError(f"Bloc {i + 1} ('{bloc}') doit être une valeur hexadécimale entre 0 et FFFF.")
		return "IPv6"
	else:
		raise ValueError("Format inconnu. Ce n'est ni une IPv4 ni une IPv6.")


def valider_liste_adresses_ip(adresses):
	adresses_valides = []
	erreurs = []

	for adresse in adresses:
		try:
			type_ip = valider_adresse_ip(adresse)
			adresses_valides.append((adresse, type_ip))
		except ValueError as e:
			erreurs.append((adresse, str(e)))

	return adresses_valides, erreurs


def valider_dictionnaire_adresses_ip(dictionnaire_adresses):
	adresses_valides = {}
	adresses_invalides = {}

	for host, adresse in dictionnaire_adresses.items():
		try:
			type_ip = valider_adresse_ip(adresse)
			adresses_valides[host] = (adresse, type_ip)
		except ValueError as e:
			adresses_invalides[host] = (adresse, str(e))

	return adresses_valides, adresses_invalides


def main():
	print("Bienvenue dans l'application de validation des adresses IP !")
	print("1 - Valider une seule adresse IP")
	print("2 - Valider une liste d'adresses IP")
	print("3 - Valider un dictionnaire d'hôtes et d'adresses IP")
	choix = input("Entrez votre choix (1, 2 ou 3) : ").strip()

	if choix == "1":
		# Valider une seule adresse IP
		adresse = input("\nEntrez une adresse IP (IPv4 ou IPv6) : ").strip()
		try:
			type_ip = valider_adresse_ip(adresse)
			print(f"L'adresse {type_ip} '{adresse}' est valide.")
		except ValueError as e:
			print(f"L'adresse '{adresse}' est invalide. Erreur : {e}")

	elif choix == "2":
		# Valider une liste d'adresses IP
		print("\nEntrez les adresses IP (une par ligne). Tapez 'FIN' pour terminer :")
		adresses = []
		while True:
			entree = input("> ").strip()
			if entree.upper() == "FIN":
				break
			adresses.append(entree)

		valides, erreurs = valider_liste_adresses_ip(adresses)

		print("\nAdresses IP valides :")
		for adresse, type_ip in valides:
			print(f"  - {adresse} ({type_ip})")

		print("\nAdresses IP invalides :")
		for adresse, erreur in erreurs:
			print(f"  - {adresse} (Erreur : {erreur})")

	elif choix == "3":
		# Valider un dictionnaire d'hôtes et d'adresses IP
		print("\nEntrez les hôtes et leurs adresses IP (format : host=adresse). Tapez 'FIN' pour terminer :")
		dictionnaire_adresses = {}
		while True:
			entree = input("> ").strip()
			if entree.upper() == "FIN":
				break
			if "=" in entree:
				host, adresse = entree.split("=", 1)
				dictionnaire_adresses[host.strip()] = adresse.strip()
			else:
				print("Format invalide. Entrez sous la forme 'host=adresse'.")

		valides, invalides = valider_dictionnaire_adresses_ip(dictionnaire_adresses)

		print("\nHôtes avec adresses IP valides :")
		for host, (adresse, type_ip) in valides.items():
			print(f"  - {host} : {adresse} ({type_ip})")

		print("\nHôtes avec adresses IP invalides :")
		for host, (adresse, erreur) in invalides.items():
			print(f"  - {host} : {adresse} (Erreur : {erreur})")

	else:
		print("Choix invalide. Veuillez entrer 1, 2, ou 3.")


if __name__ == "__main__":
	main()
