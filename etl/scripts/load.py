import pandas as pd
from sqlalchemy import create_engine, exc
import os

# Récupération des informations de connexion à la base de données depuis les variables d'environnement
host = os.getenv('POSTGRES_HOST')
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
database = os.getenv('POSTGRES_DB')

def load_data_to_postgres(filepath, table_name):
    try:
        # Création de l'engine SQLAlchemy
        engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{database}')
        
        # Lecture du fichier CSV
        data = pd.read_csv(filepath)
        
        # Insertion des données dans la base de données
        data.to_sql(table_name, engine, if_exists='append', index=False)
        
        # Affichage d'un message de confirmation en cas de succès
        print(f"Données chargées avec succès dans la table '{table_name}' depuis le fichier '{filepath}'.")

    except pd.errors.EmptyDataError:
        print(f"Erreur : Le fichier '{filepath}' est vide.")
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filepath}' est introuvable.")
    
    except exc.SQLAlchemyError as e:
        print(f"Erreur SQLAlchemy lors du chargement des données dans la table '{table_name}' : {e}")
    
    except Exception as e:
        print(f"Une erreur est survenue lors du chargement des données dans la table '{table_name}' : {e}")

if __name__ == "__main__":
    try:
        # Chargement des données dans la table 'customers'
        load_data_to_postgres('../data/raw/customer_data.csv', 'customers')
        
        # Chargement des données dans la table 'products'
        load_data_to_postgres('../data/raw/product_data.csv', 'products')
        
        # Chargement des données dans la table 'sales'
        load_data_to_postgres('../data/cleaned/cleaned_sales.csv', 'sales')
        
    except Exception as e:
        print(f"Une erreur critique est survenue : {e}")
