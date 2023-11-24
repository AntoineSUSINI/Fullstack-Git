import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models.database import SQLALCHEMY_DATABASE_URL
from importers.csv_import import MusicVideo  # Assurez-vous d'importer votre modèle ici
from models.database import BaseSQL

# Configuration de la connexion à la base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    # Tente de se connecter à la base de données
    engine.connect()
    print("Connexion à la base de données réussie.")
except Exception as e:
    print("Erreur lors de la connexion à la base de données : ", e)

Session = sessionmaker(bind=engine)

inspector = inspect(engine)

BaseSQL.metadata.create_all(engine)

# Vérification si la table 'music_videos' existe et est vide
if 'music_videos' in inspector.get_table_names():
    print("La table 'music_videos' existe.")
    session = Session()
    if session.query(MusicVideo).count() == 0:
        print("La table 'music_videos' est vide. Insertion des données...")

        # Lecture du fichier CSV
        df = pd.read_csv('kpop_music_videos.csv')

        # Insertion des données dans la base de données
        for index, row in df.iterrows():
            music_video = MusicVideo(
                id=index,
                date=row['Date'],
                artist=row['Artist'],
                song_name=row['Song Name'],
                korean_name=row['Korean Name'],
                director=row['Director'],
                video=row['Video'],
                type=row['Type'],
                release=row['Release']
            )
            session.add(music_video)

        session.commit()
        print("Données insérées avec succès.")
    else:
        print("La table 'music_videos' contient déjà des données. Aucune insertion nécessaire.")
    session.close()
else:
    print("La table 'music_videos' n'existe pas.")
