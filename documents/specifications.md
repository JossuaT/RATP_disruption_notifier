# **RATP_DISRUPTION_NOTIFIER**


## Présentation du Projet
Le projet se nomme "RATP_DISRUPTION_NOTIFIER". Soit un système de notification de perturbations RATP en temps réel.

#### **Objectif principal :** (Quelle problèmatique est résolue ?)
Ce système à pour objectif de prévenir l'utilisateur de perturbations potentielles qui pourraient survenir sur ses trajets quotidien (via les infrastructures de transports RATP). 
Cet outil est développer comme un projet personnel. Il répond à un besoin tout aussi personnel.


## **Fonctionnalités**

#### **Fonctions critiques**
Pour être en état de fonctionnemet, le système doit :
- Se connecter à une API fournie par le groupe RATP (PRIM)
- Récupérer les données liées aux perturbations du réseau
- Stocker ces données bruts
- Traiter ces données en fonction des trajets  quotidien de l'utilisateur (et donc filtrer les données par rapport aux lignes renseignées par l'utilsiateur)
- Retourner ces données à l'utilisateur de manière à e qu'il n'ait pas à utiliser une application de plannification de trajet
  
Tout cela, à des heures choisies par l'utilisateur.

#### Fonctions secondaires
Voici quelques fontionnalités secondaires qui pourront être ajoutées dans un second temps :
- Sauvegarde des données API en base de données (données brut, traitées et agrégées)
- Utilisation d'une structure cloud
- Mise en place d'un système de notification (notification mobile, notification par mail / par SMS)
- Création d'une interface d'échange avec le système


## Architecture Technique (Le "Comment")

#### Sources de données
Les données API seront fournies par la RATP, grâce à la platerforme PRIM (Plateforme Régionale d'Information pour la Mobilité).

Trois solutions sont possibles :
- API Calculateur Ile-de-France Mobilités - Messages Info Trafic (v2)
- API Messages Info Trafic - Requête globale
- API Messages affichés sur les écrans

#### Stack technique
Langage : Python 3.x
API : [PRIM (RATP)](https://prim.iledefrance-mobilites.fr/fr)

Si une sstructure cloud est mise en place, nous utiliserons la bibliothèque *dbt* pour la manipulation et le traitement des données.

#### Librairies clés
Voici une liste des bibliotèques clés :
- *requests* pour les appels API
- *dotenv* pour sécuriser les données sensibles (ex : clés API)
- *json* pour la manipulations de documents json

#### Flux de données
Les données sont d'abord récupérées grâce à l'API citée précedemment. Les données brut seront stockées avant d'être traitées et filtrées pour être à nouveau stockées.
Si l'on détecte des perturbations qui doivent être communiquées à l'utilisateur, nous devrons trouver un moyen de les communiquer à l'utilisateur. Le cas échéant, il faudra faire en sorte que l'utilisateur soit au courant des perturbations avant d'utiliser les transports impactés.



## Contraintes et Sécurité

#### Gestion des erreurs
Que se passe-t-il si l'API est hors ligne ? (Retry, message d'erreur).

#### Confidentialité
Les clés API seront stockées dans un fichier *secrets.txt* qui ne sera pas inclus dans le repo git.

#### Limites et quotas
Le nombre d'appel limite dépend de l'API utilisé. Pour en savoir plus, vous pourrez trouver plus d'informations en suivant ce [lien](https://prim.iledefrance-mobilites.fr/fr/ma-consommation-api).


## Livrables et Critères de Succès

#### Livrable
Le principal livrable lié à ce projet est un dépôt GitHub, qui contient l'ensemble du code permettant le bon fonctionnement du système ainsi que sa documention et (guide d'utilisation pas à pas, le présent cahier des charges, etc.).

#### Critère de succès
Le projet est réussi si l'utilisateur reçoit une donnée traitée et dans un temps assez court pour qu'il puisse évaluer l'état des perturbations et prendre des décisions en conséquence.