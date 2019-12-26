# Catégorisation automatique de questions

**Description du projet**:

[Stack Overflow](https://stackoverflow.com/questions) est un site célèbre de questions-réponses liées au développement informatique.
Lorsqu'on pose une question sur ce site, il faut entrer plusieurs tags de manière à retrouver facilement la question par la suite. 
Pour les utilisateurs expérimentés, cela ne pose pas de problème, mais pour les nouveaux utilisateurs, il pourrait être utile de suggérer 
quelques tags relatifs à la question posée.
L'objectif est donc de proposer un système de suggestion de tag pour le site, qui assigne plusieurs tags pertinents à une question.

**Données**:
* [StackExchange Explorer](https://data.stackexchange.com/stackoverflow/query/new): 
Les questions sont issues de l'outil d'export de données de StackOverflow, il s'agit de 50 000 questions choisies aléatoirement.

La requête utilisée:
```sql
SELECT Id, CreationDate, Body, Title, Tags FROM Posts WHERE PostTypeId = 1
ORDER BY Rand() ASC OFFSET 0 ROWS FETCH NEXT 50000 ROWS ONLY
```

**Livrables**:

*Notebooks*:
* [1_Preparation](1_Preparation.ipynb): Analyse exploratoire / Pré-traitement du texte avec NLTK
* [2_Modelisation](2_Modelisation.ipynb): Comparaison d'une méthode supervisée (régression logistique avec Tf-Idf) et d'une 
méthode non-supervisée (LDA)

*Autres*:
* [Rapport](Rapport.pdf): Présente les différentents traitements effectués, les résultats obtenus et la méthode utilisée pour l'API
* [Presentation](Presentation.pdf): Support de présentation en fin de projet

**API**:

[http://weber-thomas.fr/ocr/project6](http://weber-thomas.fr/ocr/project6) - Copier-coller une question de StackOverflow (sans les parties de code) et avec 
le titre.
