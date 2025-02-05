from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db import metadata  # Importer `metadata` de db.py

# Table pour les cartes
cartes_table = Table(
	"cartes",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("valeur", String, nullable=False),
	Column("couleur", String, nullable=False),
)

# Table pour les joueurs
joueurs_table = Table(
	"joueurs",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("nom", String, nullable=False),
)

# Table de distribution des cartes (relation entre joueurs et cartes)
distribution_table = Table(
	"distribution",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("joueur_id", Integer, ForeignKey("joueurs.id")),
	Column("carte_id", Integer, ForeignKey("cartes.id")),
)
