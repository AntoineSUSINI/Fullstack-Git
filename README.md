# Site regroupant tous les chansons de KPOP entre 2014 et 2020

## Présentation du projet

Ce projet a pour but de regrouper toutes les chansons de KPOP entre 2014 et 2020. Il est possible de rechercher une chanson par son nom, son artiste. Il est également possible de trier les chansons par ordre alphabétique, artiste ou par année de sortie par ordre croissant ou décroissant. 

## Composition du projet 
Dans le fichier racine se trouve les fichiers suivants :
- README.md : présentation du projet
- DOCKERFILE : fichier permettant de créer l'image docker
- docker-compose.yml : fichier permettant de lancer le projet
- requirements.txt : fichier contenant les librairies python nécessaires au projet
- .env qui contient les variables d'environnement (qui n'est pas exporté sur github)

Dans le fichier app se trouvent les fichiers suivants :
- main.py : fichier python contenant le code du projet 
Un fichier models contenant les fichiers suivants :
- database.py : fichier python contenant les fonctions permettant de se connecter à la base de données
- music_videos.py : fichier python qui insère les données dans la base de données
-  csv_import.py : fichier python qui contient la forme du fichier csv que nous utilisons et créé la table dans la base de données
Un fichier static contenant les fichiers suivants :
- index.html : fichier html contenant le code html du projet
- style.css : fichier css contenant le code css du projet
- scripts.js : fichier javascript contenant le code javascript du projet
Et enfin, un fichier assets qui se compose du logo que nous utilisons pour notre site. 

Pour lancer les containers et vérifier le fonctionnement du projet, il faut:
- Se trouver dans le fichier racine du projet
- Lancer la commande suivante : `docker-compose -f docker-compose.yml up `
- Ouvrir un navigateur et se rendre à l'adresse suivante : `http://localhost:5080/front/`


## Déroulement du projet
Dans un premier temps nous avons voulu initialiser la base de données avec ke fichier database.py dans le but de la remplir de données que nous avons récupéré sur le site Kaggle (https://www.kaggle.com/datasets/kimjihoo/kpopdb). Nous avons donc créé un fichier csv_import.py qui contient la forme du fichier csv que nous utilisons et créé la table dans la base de données. Nous avons ensuite créé un fichier music_videos.py qui insère les données dans la base de données. 

Après cette étape et avoir vérifié que nos données étaient bien stockées dans la base, nous avons créé le fichier index.html qui contient le code html du projet. Nous avons ensuite créé le fichier style.css qui contient le code css du projet. Enfin, nous avons créé le fichier scripts.js qui contient le code javascript du projet. Avec ces trois fichiers, nous avons pu créer la page web que nous souhaitions. 
Le site web est dynamique, il est possible de rechercher une chanson par son nom, son artiste. Il est également possible de trier les chansons par ordre alphabétique, artiste ou par année de sortie par ordre croissant ou décroissant.

## Difficultés rencontrées
Nous avons essayé d'implémenter une méthode d'authentification pour que l'utilisateur puisse se connecter à son compte. Pour ce faire, nous avons utiliser l'outil Keycloak qui permet de gérer l'authentification et l'autorisation. Cependant, nous n'avons pas réussi à faire fonctionner Keycloak avec notre projet.
Keycloak est prêt à l'emmploi et possède son propre container mais nous avons mal du réaliser le processus d'intégration. 

## Conclusion
Nous avons réussi à créer un site web dynamique qui permet de rechercher des chansons de KPOP par leur nom, leur artiste ou de les trier par ordre alphabétique, artiste ou par année de sortie par ordre croissant ou décroissant.
Ce projet nous a permis d'étendre nos connaissances sur Docker et les bases de données. Nous avons également pu améliorer nos compétences en python, html, css et javascript.
