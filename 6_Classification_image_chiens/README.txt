Description des fichiers:

------ Notebooks ------

. Data resizing: utilitaire pour re-dimensionner les images en 100x100 et créer les dossiers train/validation/test pour les CNN.
. Filters: illustration des effets des différents filtres.
. Size: étude des dimensions des images
. SIFT_2_breeds: Approche classique pour 2 races
. SIFT_3_breeds: Approche classique pour 3 races
. SIFT_5_breeds: Approche classique pour 5 races
. CNN_from_scratch: création d'un CNN et résultats pour 2, 3, 5, 60 et 120 races
. Transfer_learning_1: transfer learning en freezant toutes les couches de convolution, sans data augmentation
. Transfer_learning_2: transfer learning en freezant toutes les couches de convolution, avec data augmentation
. Transfer_learning_3: fine tuning en débloquant les 6 dernières couches de convolution


----- Python -----
. utils.py: fichier avec des fonctions utilisées dans les notebooks
. classify_5: programme de classification pour 5 races
. classify_60: programme de classification pour 60 races
. classify_120: programme de classification pour 120 races


Pour utiliser les notebooks il faut rajouter les images: http://vision.stanford.edu/aditya86/ImageNetDogs/
dans un dossier images (pour l'approche classique)
Utiliser le notebook "Data resizing" pour convertir les images en 100x100 pour l'approche CNN

