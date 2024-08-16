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

> N'hésitez pas à partager vos suggestions et à participer activement au développement de ce projet !
