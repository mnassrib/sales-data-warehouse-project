import pandas as pd

def clean_sales_data(filepath):
    try:
        # Lecture des données du fichier CSV
        sales_data = pd.read_csv(filepath)
        product_data = pd.read_csv('../data/raw/product_data.csv')

        # Merge des données de vente avec les données produit pour obtenir les coûts
        sales_data = sales_data.merge(product_data[['product_id', 'price', 'cost']], on='product_id', suffixes=('_sale', '_product'))

        # Calcul du revenu
        sales_data['revenue'] = sales_data['quantity'] * sales_data['price_sale']

        # Calcul de la marge bénéficiaire
        sales_data['profit_margin'] = ((sales_data['price_sale'] - sales_data['cost']) / sales_data['price_sale']) * 100

        # Suppression des valeurs manquantes
        sales_data.dropna(inplace=True)

        # Suppression de la colonne 'cost' puisqu'elle est product_data 
        sales_data = sales_data.drop(columns=['cost'])

        # Suppression de la colonne 'sale_id' si elle existe
        if 'sale_id' in sales_data.columns:
            sales_data = sales_data.drop(columns=['sale_id'])

        return sales_data

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filepath}' est introuvable.")
        return None

    except pd.errors.EmptyDataError:
        print(f"Erreur : Le fichier '{filepath}' est vide.")
        return None

    except KeyError as e:
        print(f"Erreur : La colonne {e} est manquante dans le fichier CSV.")
        return None

    except Exception as e:
        print(f"Une erreur est survenue lors du nettoyage des données : {e}")
        return None

if __name__ == "__main__":
    cleaned_sales_data = clean_sales_data('../data/processed/processed_sales.csv')

    if cleaned_sales_data is not None:
        try:
            # Enregistrement des données nettoyées dans un nouveau fichier CSV
            cleaned_sales_data.to_csv('../data/cleaned/cleaned_sales.csv', index=False)
            print("Les données ont été nettoyées et enregistrées avec succès dans '../data/cleaned/cleaned_sales.csv'.")
        
        except Exception as e:
            print(f"Une erreur est survenue lors de l'enregistrement du fichier CSV : {e}")
