# Prédiction du retard d'avions

**Description du projet**:

Afin d'anticiper les retards et d'optimiser la logistique, une compagnie nous demande d'analyser des données de vols 
pour évaluer les comportements de différentes compagnies aériennes.
L'objectif de cette évaluation est de tirer un premier modèle de prédiction des retards à partir des variables fournies.

**Données**:
* [Données 2016](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Anticipez+le+retard+de+vol+des+avions+-+109/Dataset+Projet+4.zip) 
: Les données représentent les informations de tous les vols nationaux aux Etats-Unis en 2016 (environ 5 600 000 vols). 
Les fichiers sont donnés mois par mois. Il y a un problème avec le mois d'avril, qu'il faut télécharger à nouveau ici: [Transtats](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time)

**Livrables**:

*Notebooks*:
* [1_Exploration](1_Exploration.ipynb): Analyse exploratoire / Nettoyage / Nouvelles variables / Export des données par compagnie
* [2_Modelisation](2_Modelisation.ipynb): Test de différents encodings / Comparaison des modèles de régression pour la prédiction

*Autres*:
* [Presentation](Presentation.pdf): Support de présentation en fin de projet


**API**:

Disponible à cette adresse: [API Prédiction retard vol](http://weber-thomas.fr/ocr/project4)
