import pandas as pd

def extract_sales_data():
    try:
        # Lecture des fichiers CSV pour 2022 et 2023
        sales_2022 = pd.read_csv('../data/raw/sales_2022.csv')
        sales_2023 = pd.read_csv('../data/raw/sales_2023.csv')
        
        # Concaténation des données
        combined_sales = pd.concat([sales_2022, sales_2023])
        return combined_sales

    except FileNotFoundError as e:
        print(f"Erreur : Le fichier est introuvable - {e.filename}")
        return None

    except pd.errors.EmptyDataError as e:
        print(f"Erreur : Le fichier est vide - {e}")
        return None

    except Exception as e:
        print(f"Une erreur est survenue lors de l'extraction des données : {e}")
        return None

if __name__ == "__main__":
    # Extraction des données
    sales_data = extract_sales_data()

    if sales_data is not None:
        try:
            # Enregistrement des données concaténées dans un nouveau fichier CSV
            sales_data.to_csv('../data/processed/processed_sales.csv', index=False)
            print("Les données ont été extraites et enregistrées avec succès dans '../data/processed/processed_sales.csv'.")
        
        except Exception as e:
            print(f"Une erreur est survenue lors de l'enregistrement du fichier CSV : {e}")
