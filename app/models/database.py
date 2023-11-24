import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Branchement de la base de données 
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

#Ajout du modèle SQLALchemy
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/{POSTGRES_DB}"

#Création de la base de données
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

BaseSQL = declarative_base()
#BaseSQL.metadata.create_all(engine)

#Base.metadata.create_all(engine)
#Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

