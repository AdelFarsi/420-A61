# Préparation de la solution d'IA pour la mise en production

Ce projet vise à mettre en production un modèle de 
régression entraîné sur le jeu de données Ames Housing. L’objectif est de prédire le prix de vente 
d’une maison à partir de ses caractéristiques, en exposant le modèle via une API REST développée 
avec Flask. 
Le projet est structuré en deux packages principaux : 
• Le package regression_model contient le pipeline de traitement, le modèle de régression et 
les scripts de prédiction. 
• Le package ml_api regroupe l’API Flask, la validation des données via Pydantic, les tests 
unitaires et les endpoints /predict et /version. 

# Conclusion :
Le projet est désormais fonctionnel : l’API répond correctement aux requêtes, le modèle retourne des prédictions cohérentes, et l’ensemble est versionné sur GitHub. Ce travail permet de simuler un déploiement réel d’un modèle de machine learning dans un environnement contrôlé.
