from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from databases import Database

# URL de la base de données SQLite
DATABASE_URL = "sqlite+aiosqlite:///./cartes.db"

# Initialisation de l'engine asynchrone et de la connexion Database
engine = create_async_engine(DATABASE_URL, echo=True)
database = Database(DATABASE_URL)

# Métadonnées communes pour SQLAlchemy
metadata = MetaData()  # Définition centrale du metadata

# Fonction pour initialiser les tables dans la base de données
async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(metadata.create_all)
