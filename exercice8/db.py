from sqlalchemy import create_engine, MetaData
from databases import Database

# Chemin de la base de données SQLite
DATABASE_URL = "sqlite:///./cartes.db"

# Initialisation de SQLAlchemy
database = Database(DATABASE_URL)  # Base de données asynchrone
engine = create_engine(DATABASE_URL)  # Moteur SQLAlchemy pour migration, etc.

metadata = MetaData()  # Métadonnées communes

def init_db():
	metadata.create_all(bind=engine)