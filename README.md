Ce projet est un système de surveillance des prix du site lalibrairie.com

Les différentes étapes de la conception de ce projet :

- Etape 1 : ecrire un script qui se rend sur une des pages produits du site et exporte ses données:
    - product_page_url
    - title
    - autor
    - price
    - product_description
    - resume
    - collection
    - image_url
    Inscrit ces colonnes et les données correspondant dans un fichier csv

- Etape 2 : Ecrire un script qui récupère les URLs de toutes une catégorie et les inscrit dans un fichier csv (voir pour post et pagination)

- Etape 3 : Ecrire un script qui éxecute les actions de l'étape 1 sur toutes les URLS recupérer dans l'étape 2

- Etape 4 : ajouter la pagination au précédent script

- Etape 5 : Créer un programme où l'utilisateur pourra choisir la catégorie qu'il souhaite