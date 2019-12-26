# Octave Convolution

**Description du projet**:
Le domaine du machine learning, et plus généralement de la data science évolue très rapidement. Il est donc important de prendre 
l'habitude de se tenir au courant des avancées et d'être capable de tester l'efficacité des nouvelles méthodes, à l'aide de 
'proof-of-concepts' (POCs)

La méthode étudiée ici est une alternative à l'opérateur de convolution utilisé habituellement dans les réseaux neuronaux convolutifs 
(CNNs), appelée l'[Octave Convolution](https://arxiv.org/pdf/1904.05049v2.pdf).

L'objectif sera d'implémenter cette méthode et de tester ses performances sur de la classification d'images avec 
un ou plusieurs datasets.

L'implémentation utilisée est celle de koshian2: 
[https://github.com/koshian2/OctConv-TFKeras](https://github.com/koshian2/OctConv-TFKeras)

**Données**:
* [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html): Dataset classique avec 60 000 images en 32x32 sur 10 classes
* [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/): 
Contient plus de 20 000 photos de chiens, réparties sur 120 races différentes. 

**Code**:
* [models](models.py): Implémentation de l'octave convolution 
(voir [https://github.com/koshian2/OctConv-TFKeras](https://github.com/koshian2/OctConv-TFKeras))
* [oct_conv2d](oct_conv2d.py): 
Implémentation de l'octave convolution (voir [https://github.com/koshian2/OctConv-TFKeras](https://github.com/koshian2/OctConv-TFKeras))
* [utils](utils.py): Liste de fonctions utilitaires

**Livrables**:

*Notebooks*:
* [7_layers_cifar](7_layers_cifar.ipynb): Test sur CIFAR-10 avec un CNN à 7 couches
* [7_layers_dogs](7_layers_dogs.ipynb): Test sur Stanford Dogs Dataset avec un CNN à 7 couches
* [9_layers_cifar](9_layers_cifar.ipynb): Test sur CIFAR-10 avec un CNN à 9 couches
* [9_layers_dogs](9_layers_dogs.ipynb): Test sur Stanford Dogs Dataset avec un CNN à 9 couches
* [nin_cifar](nin_cifar.ipynb): Test sur CIFAR-10 avec un CNN de type NIN 
(Network-In-Network: [https://arxiv.org/abs/1312.4400](https://arxiv.org/abs/1312.4400))
* [nin_dogs](nin_dogs.ipynb): Test sur Stanford Dogs Dataset avec un CNN de type NIN 
* [wrn_cifar](wrn_cifar.ipynb): Test sur CIFAR-10 avec un CNN de type WideResNet 
([https://arxiv.org/abs/1605.07146](https://arxiv.org/abs/1605.07146))
* [wrn_dogs](wrn_dogs.ipynb): Test sur Stanford Dogs Dataset avec un CNN de type WideResNet

*Autres*:
* [Presentation](Presentation.pdf): Support de présentation en fin de projet
* [Rapport](Rapport.pdf): Présentant la thématique, l'état de l'art, les jeux de données choisis, la méthode implémentée et 
les performances obtenues avec une analyse des résultats (et des échecs)
