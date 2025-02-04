# ip_operations.py

class IPv4Validator:
	def __init__(self, adresse_ipv4=None):
		"""
        Initialise la classe avec une éventuelle adresse IPv4.
        :param adresse_ipv4: Optionnel - Une adresse IPv4 sous forme de chaîne
        """
		self.adresse_ipv4 = adresse_ipv4

	def definir_adresse(self, adresse_ipv4):
		"""
        Définit une adresse IPv4 à valider ou traiter.
        :param adresse_ipv4: Adresse IPv4 sous forme de chaîne
        """
		self.adresse_ipv4 = adresse_ipv4

	def afficher_adresse(self):
		"""
        Affiche l'adresse IPv4 définie.
        """
		if self.adresse_ipv4:
			print(f"Votre adresse IP définie est : {self.adresse_ipv4}")
		else:
			print("Aucune adresse IP définie.")

	@staticmethod
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

	def valider_adresse(self):
		"""
        Valide l'adresse IPv4 définie dans l'objet.
        :return: True si l'adresse est valide, sinon déclenche une exception ValueError.
        """
		if not self.adresse_ipv4:
			raise ValueError("Aucune adresse IP n'a été définie dans l'objet.")
		return self.valider_ipv4(self.adresse_ipv4)


if __name__ == "__main__":
	# Exemple pour tester les fonctionnalités directement dans ce fichier
	print("Exemple d'utilisation de la classe IPv4Validator")
	ipv4_validator = IPv4Validator("192.168.1.1")
	ipv4_validator.afficher_adresse()
	try:
		if ipv4_validator.valider_adresse():
			print("L'adresse est valide.")
	except ValueError as e:
		print(f"Erreur : {e}")
