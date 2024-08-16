# Utiliser une image Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /etl

# Installer wget
RUN apt-get update && apt-get install -y wget

# Télécharger et installer Dockerize
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz -O /usr/local/bin/dockerize.tar.gz \
    && tar -C /usr/local/bin -xzf /usr/local/bin/dockerize.tar.gz \
    && mv /usr/local/bin/dockerize /usr/local/bin/dockerize-linux-amd64 \
    && chmod +x /usr/local/bin/dockerize-linux-amd64 \
    && rm /usr/local/bin/dockerize.tar.gz

# Installer les dépendances à partir de requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour attendre PostgreSQL et exécuter les scripts ETL
CMD ["/usr/local/bin/dockerize-linux-amd64", "-wait", "tcp://postgres:5432", "-timeout", "60s", "bash", "-c", "python /etl/extract.py && python /etl/transform.py && python /etl/load.py"]
