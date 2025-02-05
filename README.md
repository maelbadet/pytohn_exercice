# Description du repo

Le repo est constituee de plusieurs sous fichiers dans lesquels sont mis mes different exercices pythons.

Le venv est creer automatiquement, car j'utilise Pycharm.

## Exercice 1
Dans le sous-dossier exercice 1, on retrouvera :

- Exercice 1 : script pour demander à un utilisateur de rentrer une IPv4,
- Exercice 2 : script pour verifier l'adresse IPv4 rentrer par l'utilisateur,
- Exercice 3 : script pour verifier l'adresse IPv6 rentrer par l'utilisateur,
- Exercice 4 : script pour creer une methode pour verifier quel type d'adresse IP est envoyé, si elle est valide et renvoyer à l'utilisateur quelle version d'IP, il a envoyé,
- Exercice 5 : script pour faire la meme chose que l'exercice 4, mais avec une liste et un dictionnaire statique,
- Exercice 6 : script pour demander à un utilisateur de rentrer un chiffre pour choisir ce qu'il veut :
  - 1 : rentrer une adresse IP simple
  - 2 : rentrer une liste d'adresse IP
  - 3 : rentrer un dictionnaire d'adresse IP

## Exercice 2 :
Le but de cet exercice est de travailler sur les modifications de fichiers
- Exercice 1 : script pour remplacer chaque voyelle par un 'x' dans le fichier text donner
- Exercice 2 : script pour lire un fichier text et retourner : 
  - Son numero de ligne
  - son nombre de caractere
  - le contenu de sa ligne

## Exercice 3
Dans cette exerice, on va faire plusieurs choses. 
On va commencer à jouer avec les api sur des requetes GET ou POST (j'ai choisi GET personnellement),
de plus, on va jouer avec les exports de fichier en changeant d'extension (passer d'un txt a un json ou un csv, etc.).

- Exercice 1 : j'ai utilisé l'api `https://api.fbi.gov/wanted/v1/list`, 
pour recuperer les 3 premiere personnes rechéché par le fbi de la page numero 2
- Exercice 2 : mon script permet de lire un fichier csv et de changer ses id en incrementant de +1 celui de base.
- Exercice 3 : Ce script permet de pouvoir lire le fichier text que j'ai dans le dossier text_files et de sauvegarder 
ce fichier dans mon dossier json_files sous un format json et non plus text
- Exercie 4 : pareil que pour l'exercice 4, mais dans le dossier csv_files en format csv

## Exercice 4
Dans cet exercice, le but est de commencer à se familiariser avec la POO sur python.
- question 1, dans ce script, je reprends la question de l'exercice 1 pour envoyer une adresse IP, mais en utilisant un module pour pouvoir le reutiliser
- question 2, pareil que pour la question 1, mais en faisant une classe pour ajouter les fonctionnalites
- question 3, là, le but est de faire une petite application bancaire pour comprendre le principe d'heritage de classe et de modules

## Exercice 5
Le but de cet exercice est de faire un petit jeu de cartes dans lequel on jouera avec 52 cartes
definie au lancement pour commencer, puis et enfin distribuer selon le nombre de joueurs 
à parts egales.
- question 1, le script permettant de generer le paquet de 52 cartes avec numero et couleurs
- question 2, le script permettant de melanger le paquet de carte, il doit etre unique à chaque appel
- question 3, le fait de demander le nombre de joueurs et attribuer un nombre de cartes egales pour chaque joueur et afficher le reste si besoin

## Exercice 6 
Avant toute chose, penser à installer pytest si ce n'est pas deja fais :` pip install pytest`
Une fois pytest installer, on peut tester les deux manieres de faire les tests sur python : 
- via la main.py pour le test avec les `assert`
- en faisant la commande pytest -v depuis le bon dossier (exercice 6) pour les tests avec pytest

## Exercice 7 
Pareil que pour l'exercice 6, bien verifier que fastapi et uvicorn sont bien installées avant de faire des tests : `   pip install fastapi uvicorn`
Une fois ça fait : je mets en dessous les differentes routes pour les differents projet : 
pour lancer le serveur pour l'api, il suffit de taper cette commande dans le bon sous dossier que je liste ci-dessous
- premiere_api_fast_api : 
  - Connexion : 127.0.0.1:8000 ou localhost:8000
  - route (/) : affiche un message de bienvenu dans mon api
  - route (/tiems) : affiche tous les items definies dans ma liste statique
  - route (/items/item_id) : affiche l'item par son id ou renvoie une 404 en cas d'item non trouver
- jeux_52_cartes_fastAPI : 
  - Connexion : 127.0.0.1:8000 ou localhost:8000
  - route (/) : affiche un message de bienvenu
  - route (/cartes/) : affiche les toutes les cartes
  - route (/cartes/melangees/) : affiche toutes les cartes melangees
  - route (/cartes/distribution/?nb_joueur=`mettre le nombre de joueur`) : affiche la distribution de cartes
  
Commande pour lancer le serveur : `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
## Exercice 8
