def valider_ipv6(adresse_ipv6):
	"""
	Vérifie si une adresse IPv6 est valide.
	:param adresse_ipv6: Adresse IPv6 sous forme de chaîne
	:return: True si l'adresse est valide, sinon déclenche une exception ValueError
	"""
	# Diviser l'adresse par les séparateurs ':'
	blocs = adresse_ipv6.split(":")

	# Règle 1 : Vérifier la longueur (certaines adresses raccourcies peuvent avoir moins de blocs)
	if len(blocs) > 8:
		raise ValueError("L'adresse IPv6 ne peut pas contenir plus de 8 blocs.")

	# Règle 2 : Gérer le cas du raccourci "::"
	if "" in blocs:
		# Vérifier la validité de "::"
		if adresse_ipv6.count("::") > 1:
			raise ValueError("L'adresse IPv6 ne peut contenir qu'un seul raccourci '::'.")
		elif adresse_ipv6 == "::":
			return True  # Cas spécial : l'adresse "::" est valide

		# Remplacer "::" par un nombre approprié de blocs de zéros pour simplifier les vérifications
		index_double_colon = blocs.index("")
		blocs.pop(index_double_colon)  # Supprimer le bloc vide
		while len(blocs) < 8:
			blocs.insert(index_double_colon, "0")  # Ajouter des blocs de zéros

	# Règle 3 : Valider chaque bloc
	for i, bloc in enumerate(blocs):
		if bloc == "":
			continue  # Un bloc vide est autorisé à cause de "::"
		if len(bloc) > 4:
			raise ValueError(f"Bloc {i + 1} ('{bloc}') contient plus de 4 caractères hexadécimaux.")
		try:
			# Vérifiez si chaque bloc est un nombre hexadécimal valide
			valeur = int(bloc, 16)
			if valeur < 0 or valeur > 0xFFFF:
				raise ValueError(f"Bloc {i + 1} ('{bloc}') n'est pas compris entre 0 et FFFF.")
		except ValueError:
			raise ValueError(f"Bloc {i + 1} ('{bloc}') n'est pas un nombre hexadécimal valide.")

	# Si toutes les validations passent, renvoyer True
	return True


def main():
	print("Bienvenue dans l'application de validation des adresses IP !")

	# Entré utilisateur
	adresse_ip = input("Veuillez entrer une adresse IP (IPv4 ou IPv6) : ").strip()

	try:
		# Détection IPv4 ou IPv6
		if ":" in adresse_ip:
			valider_ipv6(adresse_ip)
			print(f"L'adresse IPv6 {adresse_ip} est valide.")
		else:
			raise ValueError("Format d'adresse inconnu. Ce n'est ni une IPv4 ni une IPv6.")

	except ValueError as e:
		# Gestion des erreurs : afficher un message clair
		print(f"Erreur : {e}. Veuillez entrer une adresse IP valide.")


if __name__ == "__main__":
	main()
