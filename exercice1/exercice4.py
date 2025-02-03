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

	# Détecter si c'est une adresse IPv6 (présence de ":")
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

	# Entré utilisateur
	adresse_ip = input("Veuillez entrer une adresse IP (IPv4 ou IPv6) : ").strip()

	try:
		# Valider l'adresse IP
		type_ip = valider_adresse_ip(adresse_ip)
		print(f"L'adresse {type_ip} {adresse_ip} est valide.")
	except ValueError as e:
		print(f"Erreur : {e}. Veuillez entrer une adresse IP valide.")


if __name__ == "__main__":
	main()
