# Sales Data Warehouse Project

## Introduction

### Intérêt et vision d'un entrepôt de données

Un entrepôt de données (Data Warehouse) est une infrastructure essentielle pour toute entreprise cherchant à exploiter pleinement ses données. Il centralise les informations provenant de multiples sources, permettant ainsi une analyse approfondie et une prise de décision éclairée. L'entrepôt de données est conçu pour stocker de grandes quantités de données sur une longue période, facilitant les analyses historiques et prévisionnelles. Son objectif principal est de fournir une vue globale et unifiée des opérations de l'entreprise, afin d'améliorer l'efficacité, identifier des opportunités commerciales, et optimiser les processus.

### Pourquoi utilisons-nous Docker ?

Docker est un outil puissant qui permet de créer, déployer et exécuter des applications dans des conteneurs légers et portables. En utilisant Docker, nous nous assurons que l'application fonctionne de manière identique, quelle que soit l'environnement de déploiement. Cela élimine les problèmes de compatibilité et facilite grandement la gestion des dépendances, le déploiement et la mise à l'échelle de l'application. Dans ce projet, Docker est utilisé pour conteneuriser les différents services (ETL, PostgreSQL, Metabase, Superset) afin de les exécuter de manière cohérente et indépendante sur n'importe quel système.

## Contexte du projet

### Analyse des ventes d'une entreprise

Ce projet est centré sur l'analyse des ventes d'une entreprise fictive. L'objectif est de simuler un environnement réaliste avec des données de ventes provenant de plusieurs années pour illustrer comment un entrepôt de données peut transformer des données brutes en insights exploitables. Les données sont stockées dans des fichiers CSV, traitées par un pipeline ETL automatisé, et enfin visualisées à l'aide de deux outils puissants : Metabase et Superset.

### Structure du projet

Le projet est organisé de manière modulaire pour en faciliter la gestion et l'évolutivité. Voici la structure du projet :

```
sales-data-warehouse-project/
│
├── data/
│   ├── raw/                  # Données brutes
│   │   ├── sales_2022.csv
│   │   ├── sales_2023.csv
│   │   ├── product_data.csv
│   │   └── customer_data.csv
│   ├── processed/            # Données après la phase d'extraction
│   │   └── processed_sales.csv
│   └── cleaned/              # Données nettoyées après transformation
│       └── cleaned_sales.csv
├── etl/
│   ├── scripts/              # Scripts ETL
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   ├── Dockerfile            # Dockerfile pour le service ETL
│   └── requirements.txt      # Dépendances Python pour ETL
├── init/
│   └── init.sql              # Script d'initialisation pour PostgreSQL
├── superset/
│   ├── init_superset.py      # Script d'initialisation pour Superset
│   └── superset_config.py    # Configuration de Superset
├── .env                      # Fichier d'environnement pour les variables sensibles
├── docker-compose.yml        # Fichier Docker Compose pour orchestrer les services
└── README.md                 # Ce fichier de documentation
```

## Explication des données

### Fichier `sales_2022.csv` et `sales_2023.csv`

Ces fichiers contiennent les données de vente pour les années 2022 et 2023. Les colonnes incluent :

- **sale_id** : Identifiant unique de la vente.
- **product_id** : Identifiant du produit vendu.
- **customer_id** : Identifiant du client ayant effectué l'achat.
- **quantity** : Quantité de produits vendus.
- **sale_date** : Date de la vente.
- **price** : Prix de vente par unité du produit au moment de la vente.

### Fichier `product_data.csv`

Ce fichier contient les informations sur les produits vendus. Les colonnes incluent :

- **product_id** : Identifiant unique du produit.
- **product_name** : Nom du produit.
- **category** : Catégorie du produit.
- **price** : Prix de vente recommandé du produit.
- **cost** : Coût de production ou d'acquisition du produit.

### Fichier `customer_data.csv`

Ce fichier contient les informations sur les clients. Les colonnes incluent :

- **customer_id** : Identifiant unique du client.
- **customer_name** : Nom du client.
- **age** : Âge du client.
- **gender** : Sexe du client.
- **email** : Adresse email du client.
- **city** : Ville de résidence du client.
- **country** : Pays de résidence du client.

## Le projet comme un entrepôt de données (data warehouse)

Ce projet illustre parfaitement le concept d'un entrepôt de données. Les données provenant de différentes sources (fichiers CSV) sont centralisées dans une base de données relationnelle (PostgreSQL). Ce processus de centralisation permet d'unifier les données disparates pour les analyser de manière cohérente et complète. L'entrepôt de données ainsi créé est capable de répondre à des requêtes complexes et de fournir des analyses historiques et prévisionnelles pour soutenir la prise de décision.

## Le processus automatisé : pipeline ETL (Extract, Transform, Load)

### Qu'est-ce qu'un pipeline ETL ?

Le pipeline ETL (Extract, Transform, Load) est un processus essentiel dans la gestion des données. Il s'agit d'un processus automatisé qui extrait les données brutes de différentes sources, les transforme en appliquant des nettoyages et des calculs nécessaires, et les charge dans une base de données prête à être utilisée pour des analyses et visualisations. 

### Comment ce pipeline ETL est-il configuré pour être automatisé ?

Dans ce projet, le pipeline ETL est entièrement automatisé grâce à Docker et Docker Compose. Chaque étape du pipeline (extraction, transformation, chargement) est gérée par des scripts Python spécifiques, et le tout est orchestré par Docker. Le fichier `docker-compose.yml` définit les services nécessaires et spécifie les commandes à exécuter pour automatiser le pipeline. Ce pipeline peut être déclenché automatiquement lors du démarrage des services Docker, garantissant ainsi que les données sont toujours à jour.

### Explication des données et des différences de prix

Il est crucial de comprendre la différence entre le **prix de vente** (price dans les fichiers de ventes) et le **prix du produit** (price dans le fichier des produits). Le prix de vente correspond au montant payé par le client au moment de l'achat, qui peut inclure des remises ou autres ajustements. En revanche, le prix du produit est le prix standard ou recommandé pour le produit. Cette différence est fondamentale pour le calcul des marges bénéficiaires.

### Marges bénéficiaires et autres analyses internes

Les marges bénéficiaires sont calculées en comparant le coût du produit au prix de vente réel. La marge bénéficiaire est un indicateur clé pour évaluer la rentabilité d'un produit ou d'une vente. Dans ce projet, la marge bénéficiaire est calculée comme suit :

\[ \text{Marge bénéficiaire (\%)} = \left(\frac{\text{Prix de vente} - \text{Coût}}{\text{Prix de vente}}\right) \times 100 \]

Cette analyse permet d'identifier les produits les plus rentables, de mieux comprendre les tendances de vente, et de prendre des décisions stratégiques.

## Pourquoi l'idée de suggérer à la fois Metabase et Superset dans ce même projet ?

Metabase et Superset sont deux outils complémentaires pour l'analyse de données. 

- **Metabase** est facile à utiliser pour les utilisateurs non techniques et permet de créer rapidement des tableaux de bord interactifs.
- **Superset** est plus flexible et adapté aux utilisateurs techniques, offrant des fonctionnalités avancées pour des visualisations plus complexes.

En utilisant ces deux outils, vous pouvez satisfaire les besoins de différents types d'utilisateurs au sein de l'entreprise, qu'ils soient analystes métiers ou data scientists.

## Comment faire fonctionner ce projet ?

### Services et démarrage

Le projet est orchestré à l'aide de Docker Compose, ce qui simplifie grandement le déploiement et la gestion des services. Voici comment démarrer le projet :

1. **Configurer l'environnement** : Assurez-vous que le fichier `.env` contient les informations correctes pour les bases de données et les services.
2. **Démarrer les services** : Exécutez `docker-compose up --build` pour construire et démarrer les services.
3. **Vérifier les services** : Une fois les services démarrés, vous pouvez accéder aux différentes interfaces pour gérer et analyser les données.

### Accès aux services via un navigateur

Les différents services sont accessibles via les URL suivantes dans un navigateur :

- **PgAdmin** : [http://localhost:8080](http://localhost:8080) — Interface pour gérer la base de données PostgreSQL.
- **Metabase** : [http://localhost:3000](http://localhost:3000) — Interface pour créer des tableaux de bord interactifs.
- **Superset** : [http://localhost:8088](http://localhost:8088) — Interface pour des analyses avancées et des visualisations de données.

### Explications sur le fonctionnement de chaque outil

- **PgAdmin** : Cet outil est utilisé pour gérer et administrer la base de données PostgreSQL. Il permet de visualiser la structure des tables, d'exécuter des requêtes SQL, de gérer les utilisateurs et les permissions, et d'effectuer des opérations de maintenance sur la base de données. C'est un outil essentiel pour les administrateurs de base de données.

- **Metabase** : Metabase est une plateforme de business intelligence qui permet de créer des tableaux de bord interactifs et des rapports sans nécessiter de compétences avancées en SQL. Les utilisateurs peuvent poser des questions en langage naturel, explorer les données, et créer des visualisations pour aider à comprendre les performances de l'entreprise. Metabase est particulièrement apprécié pour sa facilité d'utilisation et sa capacité à permettre à des utilisateurs non techniques de tirer parti des données.

- **Superset** : Apache Superset est un outil d'exploration et de visualisation de données qui offre une grande flexibilité et des fonctionnalités avancées. Il permet de créer des tableaux de bord complexes, de réaliser des explorations de données en profondeur, et de générer des visualisations interactives. Superset est adapté aux utilisateurs ayant des compétences en SQL ou en data science, car il permet de construire des analyses détaillées et personnalisées.

## Quel serait le prochain traitement ETL ?

Le prochain traitement ETL pourrait consister en l'intégration de nouvelles sources de données, comme des données provenant de systèmes CRM ou ERP pour enrichir les analyses. Cela pourrait inclure l'ajout de données sur les interactions client, les performances des campagnes marketing, ou encore l'intégration de données financières pour calculer des indicateurs de performance clés (KPI) plus sophistiqués.

Une autre possibilité est d'automatiser encore davantage le pipeline en intégrant des déclencheurs basés sur des événements (par exemple, lorsqu'un nouveau fichier est déposé dans un répertoire, le pipeline ETL se déclenche automatiquement). Vous pourriez aussi envisager d'optimiser les performances en déployant des index sur les tables fréquemment interrogées ou en mettant en place des mécanismes de mise en cache pour accélérer les temps de réponse des requêtes.

## Suggestions et prochaines étapes

Nous encourageons les utilisateurs à contribuer à ce projet en proposant des améliorations ou en développant de nouvelles fonctionnalités. Par exemple :

- **Extension du modèle de données** : Ajouter des données supplémentaires ou des fonctionnalités d'analyse avancées.
- **Automatisation des tests** : Intégrer des tests automatisés pour valider les transformations ETL et garantir l'intégrité des données.
- **Amélioration des visualisations** : Créer des tableaux de bord encore plus interactifs et personnalisés dans Metabase et Superset.


---
## Bon à savoir

Les termes "base de données", "entrepôt de données" et "lac de données" désignent trois concepts différents dans le domaine de la gestion des données. Voici les différences principales entre ces concepts :

### **Différences entre Base de données, Entrepôt de données et Lac de données**

#### 1. **Base de données (Database)**

##### **Définition**
Une **base de données** est un ensemble structuré d'informations ou de données, généralement organisé sous forme de tables. Ces données sont gérées via un **Système de Gestion de Base de Données (SGBD)** (*Database Management System - DBMS* en anglais), qui permet d’accéder, de manipuler et de gérer les données efficacement.

##### **Type de données**
- **Données structurées** : Organisées de manière formelle dans des tables avec des lignes et des colonnes. Chaque colonne représente un attribut, et chaque ligne représente un enregistrement.

##### **Utilisation**
Les bases de données sont principalement utilisées pour des **transactions en ligne** (en anglais : *Online Transaction Processing - OLTP*), comme :
- La gestion des clients,
- La gestion des stocks,
- Les transactions bancaires.

##### **Accès**
- **Temps réel** : Les données sont accessibles immédiatement, permettant des opérations fréquentes comme des insertions, des mises à jour, des suppressions et des requêtes.

##### **Technologies C=courantes**
- **Bases de données relationnelles (RDBMS)** :
  - **MySQL** : Gratuit, avec une version open source disponible (MySQL Community Edition). Utilisé pour des applications web, il est populaire pour sa simplicité et son efficacité.
  - **PostgreSQL** : Gratuit et entièrement open source, avec des fonctionnalités avancées telles que le support des données géographiques.
  - **MariaDB** : Un fork de MySQL, gratuit et open source.
  - **SQLite** : Gratuit, très léger, souvent utilisé pour des applications embarquées.
  - **Oracle Database** : Versions complètes payantes, bien que des versions d'essai ou des versions limitées (comme Oracle XE) soient gratuites.
  - **Microsoft SQL Server** : Intégré dans les environnements Windows, avec des fonctionnalités riches pour les entreprises. Une version gratuite est disponible avec des limitations (SQL Server Express).
  - **IBM Db2** : Principalement payant, mais offre une version gratuite limitée (*Db2 Community Edition*).

- **Bases de données NoSQL (Not Only SQL)** :
  - **MongoDB** : Base de données orientée document, idéale pour les applications nécessitant une grande flexibilité dans la structure des données.
  - **Cassandra** : Conçue pour gérer de grandes quantités de données distribuées sur plusieurs centres de données.
  - **Redis** : Base de données en mémoire, souvent utilisée pour des opérations de cache rapide.
  - **Couchbase** : Une autre base de données orientée document, avec un support pour les requêtes SQL.

#### 2. **Entrepôt de données (Data Warehouse)**

##### **Définition**
Un **entrepôt de données** est une base de données spécialisée conçue pour l'analyse et le reporting. Il regroupe des données provenant de diverses sources, les nettoie, les transforme et les structure pour permettre des analyses complexes.

##### **Type de données**
- **Données structurées** : Les données sont organisées pour être facilement interrogeables et analytiques.
- **Données historisées et agrégées** : L'entrepôt contient souvent des données sur de longues périodes pour des analyses historiques.

##### **Utilisation**
Les entrepôts de données sont utilisés pour des opérations de **traitement analytique en ligne** (en anglais : *Online Analytical Processing - OLAP*), comme :
- Les rapports financiers,
- L’analyse des tendances,
- Les prévisions.

##### **Accès**
- **Analyses complexes** : Les requêtes sont souvent plus lourdes que dans une base de données transactionnelle, et visent à extraire des informations à partir de grandes quantités de données.

##### **Technologies courantes**
- **Gratuites ou Open Source** :
  - **Apache Hive** : Gratuit, open source, utilisé pour exécuter des requêtes SQL sur des données dans Hadoop.
  - **Apache Druid** : Entrepôt de données en temps réel, open source, conçu pour des analyses OLAP rapides.
  - **ClickHouse** : Base de données analytique en colonne, open source, très performante pour les requêtes analytiques.

- **Solutions Cloud Freemium** :
  - **Amazon Redshift** : Payant, mais Amazon propose un essai gratuit de 2 mois pour une petite instance.
  - **Google BigQuery** : Payant, avec une offre gratuite qui permet un certain volume de traitement de données chaque mois.
  - **Snowflake** : Payant, avec un essai gratuit pour une durée limitée et un crédit de départ.

- **Solutions On-Premise Payantes** :
  - **Teradata** : Connu pour sa capacité à traiter des volumes massifs de données pour les grandes entreprises.
  - **Oracle Exadata** : Optimisé pour exécuter des requêtes complexes à haute performance.
  - **IBM Netezza** : Offre des performances élevées pour l’analyse des données.
  - **Microsoft SQL Server Analysis Services (SSAS)** : Composant de SQL Server utilisé pour l’analyse multidimensionnelle.
  - **Microsoft Azure Synapse Analytics** : Plateforme de données analytique intégrée sur Microsoft Azure.

#### 3. **Lac de données (Data Lake)**

##### **Définition**
Un **lac de données** est un dépôt de stockage massif capable de contenir des données de toutes formes (structurées, semi-structurées, non structurées) dans leur état brut. Contrairement à un entrepôt de données, les données dans un lac de données ne sont pas nettoyées ni transformées avant d’être stockées.

##### **Type de données**
- **Données brutes** : Stockées telles quelles, sans transformation ni structuration préalable.
- **Données hétérogènes** : Peut inclure des fichiers texte, des images, des vidéos, des flux de données en temps réel, des fichiers log, etc.

##### **Utilisation**
Les lacs de données sont particulièrement utiles pour le **big data**, l’intelligence artificielle (IA) et le machine learning, ainsi que pour des explorations de données non structurées.

##### **Accès**
- **Exploration et analyse à grande échelle** : Les données brutes nécessitent des outils et des traitements spécifiques pour être analysées efficacement.

##### **Technologies courantes**
- **Gratuites et Open Source** :
  - **Apache Hadoop** : Gratuit, open source, composant clé pour les lacs de données (inclut HDFS).
  - **Apache Spark** : Gratuit et open source, souvent utilisé pour le traitement de données dans les lacs de données.
  - **Apache Hudi** : Système de gestion de lacs de données open source, offrant des fonctionnalités pour le traitement de données à grande échelle.
  - **Presto** : Moteur de requêtes SQL open source, gratuit, utilisé pour interroger des données stockées dans un lac de données.

- **Solutions Cloud Freemium** :
  - **Amazon S3** : Payant, mais offre un niveau gratuit limité (5 Go de stockage gratuit pendant la première année).
  - **Azure Data Lake Storage** : Payant, avec un essai gratuit pour un volume limité de stockage.
  - **Google Cloud Storage** : Payant, avec un essai gratuit incluant un crédit initial et une capacité de stockage limitée.

- **Non gratuites** :
  - **Databricks** : Payant, mais il existe une version communautaire gratuite pour l'apprentissage et les tests.
  - **Cloudera** : Payant, bien qu’il existe une version gratuite pour les développeurs avec des fonctionnalités limitées.

#### **Comparatif synthétique**

| **Critère**        | **Base de données (Database)** | **Entrepôt de données (Data Warehouse)** | **Lac de données (Data Lake)**          |
|--------------------|---------------------------------|------------------------------------------|-----------------------------------------|
| **Structure**      | Structurée                      | Structurée et historisée                 | Non structurée / Brute                  |
| **Utilisation**    | Transactions (OLTP)             | Analyses (OLAP)                          | Big Data, IA, Machine Learning          |
| **Données**        | Actuelles, souvent modifiées    | Historisées, agrégées                    | Brutes, de divers formats               |
| **Technologies**   | MySQL, PostgreSQL, MongoDB      | Redshift, Snowflake, Teradata            | Hadoop, Spark, Amazon S3, Azure Data Lake |

#### **Résumé des options gratuites**

- **Bases de données** : MySQL, PostgreSQL, SQLite, MariaDB, Microsoft SQL Server Express, Oracle XE.
- **Entrepôts de données** : Apache Hive, Apache Druid, ClickHouse.
- **Lacs de données** : Apache Hadoop, Apache Spark, Apache Hudi, Presto.


Les solutions cloud comme Amazon S3, Google BigQuery, et Snowflake offrent généralement des essais gratuits ou des niveaux gratuits limités, mais deviennent payants au-delà d'un certain seuil d'utilisation. Les solutions open source sont généralement gratuites, mais nécessitent une infrastructure et une expertise technique pour être déployées et gérées efficacement.

---

> N'hésitez pas à partager vos suggestions et à participer activement au développement de ce projet !
