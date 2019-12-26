# Classification automatique d'images de chiens

**Description du projet**:
Une association de protection des animaux a une base de données de pensionnaires qui commence à s'agrandir et ils n'ont pas 
toujours le temps de référencer les images des animaux qu'ils ont accumulées depuis plusieurs années. 
Ils aimeraient donc réaliser un index de l'ensemble de la base de données d'images, pour classer les chiens par races.

**Données**:
* [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/): 
Contient plus de 20 000 photos de chiens, réparties sur 120 races différentes. 

**Livrables**:

*Notebooks*:
* [1_1_Size](1_1_Size.ipynb) et [1_2_Data_resizing](1_2_Data_resizing.ipynb): Re-dimensionnement des images à la même taille
* [2_Filters](2_Filters.ipynb): Etude de l'effet de différents filtres
* [3_1_SIFT_2_breeds](3_1_SIFT_2_breeds.ipynb), [3_2_SIFT_3_breeds](3_2_SIFT_3_breeds.ipynb) et [3_3_SIFT_5_breeds](3_3_SIFT_5_breeds.ipynb)
: Approche classique avec la méthode SIFT pour une classification sur 2, 3 ou 5 races
* [4_1_CNN_from_scratch](4_1_CNN_from_scratch.ipynb): Approche deep learning avec un réseau neuronal convolutif (CNN) sans pré-entraînement
* [4_2_Transfer_learning_1](4_2_Transfer_learning_1.ipynb), [4_3_Transfer_learning_2](4_3_Transfer_learning_2.ipynb) 
et [4_4_Transfer_learning_3](4_4_Transfer_learning_3.ipynb): Utilisation d'un réseau pré-entraîné (transfer learning) pour améliorer 
les performances de classification

*Code*:
* [classify_5](classify_5.py): Programme de classification parmi 5 races
* [classify_60](classify_60.py): Programme de classification parmi 60 races
* [classify_120](classify_120.py): Programme de classification parmi 120 races
* [utils](utils.py): Liste de fonctions utilitaires

Pour faire tourner ces programmes il faut aussi télécharger les poids des réseaux de neurones utilisés. Ils sont disponibles ici:
[5 races](https://drive.google.com/open?id=1xig2wHp15Ar5xaIDPmNmkwMpsTohG6y1), 
[60 races](https://drive.google.com/open?id=1F2d2Es2Rbvljml2mXoV2-RIsA17BTivp),
[120 races](https://drive.google.com/open?id=1H_9u7YrCcxp1cvMi_yCKJ4DHVqwwGPoD)

* Les fichiers 'classes_encoding_' servent de table de correspondance entre un id et le nom d'une race

*Autres*:
* [Presentation](Presentation.pdf): Support de présentation en fin de projet

