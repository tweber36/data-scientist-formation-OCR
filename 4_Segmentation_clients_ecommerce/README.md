# Segmentation des comportements de clients

**Description du projet**:
Un site d'e-commerce souhaite mieux comprendre les comportements de ses clients pour augmenter la fréquence d'achat et la valeur 
du panier moyen. 
L'objectif est de comprendre les différents types d'utilisateurs grâce à leur comportement dans la durée, afin de détecter les plus 
susceptibles de passer à l'achat.

**Données**:
* [dataset.csv](dataset.csv): Liste des transactions effectuées sur une année (1 ligne par transaction)

*Autres données*:
* [customers_full.csv](customers_full.csv): Données transformées pour représenter les données des clients (1 ligne par client)
* [train.csv](train.csv): Jeu d'entraînement utilisé pour les modèles de classification (issu de customers_full)
* [test.csv](test.csv): Jeu de validation pour sélectioner le modèle
* [new_clients.csv](new_clients.csv): Quelques exemples de transactions pour tester le programme final sur de nouveaux clients

**Livrables**:

*Notebooks*:
* [1_Exploration](1_Exploration.ipynb): Analyse exploratoire / Transformations en données clients / Clustering
* [2_Classification](2_Classification.ipynb): Choix du modèle de classification par validation croisée

*Code*:
* [Classify.py](classify.py): Programme de classification - prend en entrée une liste de transactions (par exemple le fichier new_clients):
```
python classify.py new_clients.csv
```
* params.pickle: Contient les paramètres des modèles utilisés par le programme de classification

*Autres*:
* [Presentation](Presentation.pdf): Support de présentation en fin de projet
