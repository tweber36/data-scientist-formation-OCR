Description des fichiers:

------ Data ------
. dogs_32 : Stanford Dogs Dataset re-dimensionné en 32x32 et séparé en 2 jeux (entraînement et test)
. history_results : dossier qui contient les historiques d'apprentissage des réseaux de neurones

------ Notebooks ------
. 7_layers_cifar.ipynb : Test avec un modèle à 7 couches sur le dataset CIFAR-10
. 7_layers_dogs.ipynb : Test avec un modèle à 7 couches sur le dataset Dogs
. 9_layers_cifar.ipynb : Test avec un modèle à 9 couches sur le dataset CIFAR-10
. 9_layers_dogs.ipynb : Test avec un modèle à 9 couches sur le dataset Dogs
. nin_cifar.ipynb : Test avec un modèle Network-in-Network sur le dataset CIFAR-10
. nin_dogs.ipynb : Test avec un modèle Network-in-Network sur le dataset Dogs
. wrn_cifar.ipynb : Test avec un modèle WideResNet sur le dataset CIFAR-10
. wrn_dogs.ipynb : Test avec un modèle WideResNet sur le dataset Dogs

----- Python -----
. models.py : fonctions utilisées pour le modèle WideResNet
. oct_conv2d.py : implémentation de l'Octave Convolution, basée sur https://github.com/koshian2/OctConv-TFKeras
. utils.py : fonctions utilitaires

----- PDFs -----
. Drop an Octave.pdf : article original sur l'Octave Convolution: https://arxiv.org/pdf/1904.05049v2.pdf
. Plan de travail.pdf : plan de travail fait au début du projet
. Rapport.pdf : rapport final

----- Autres -----
. FLOPS.xlsx : Fichier qui m'a servi à calculer le nombre de FLOPS théoriques
. Présentation.pptx : Présentation qui a servi de support à la soutenance
