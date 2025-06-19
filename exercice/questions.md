# Exercice d'Analyse de Données avec Python

## Question 1 : Compter les victimes entre 2022 et 2023

**Objectif** : Créer une fonction pour compter les victimes entre deux années spécifiques.

**Tâche** : Écrivez une fonction `compte_victimes` qui prend un DataFrame, une année minimale et une année maximale, et retourne le nombre de victimes pour cette période.

**Indices** :
- Utilisez des conditions booléennes pour filtrer les données en fonction de l'année.
- Utilisez `len()` pour compter le nombre de lignes dans le DataFrame filtré.

## Question 2 : Compter les victimes après 2022, qui sont des femmes

**Objectif** : Utiliser la fonction précédente et ajouter un paramètre pour le sexe.

**Tâche** : Modifiez la fonction `compte_victimes` pour ajouter un paramètre `sexe_victime` et utilisez-la pour compter les victimes après 2022 qui sont des femmes.

**Indices** :
- Ajoutez un paramètre optionnel `sexe_victime` à la fonction.
- Utilisez ce paramètre pour filtrer davantage les données.

## Question 3 : Compter les victimes après 2022 qui ont aussi été des mis en cause

**Objectif** : Compter de deux façons différentes les victimes après 2022 qui ont aussi été des mis en cause avant la première année où ils ont été victimes.

**Tâche** : Utilisez la fonction précédente et créez une nouvelle fonction `compte_mis_en_cause` pour compter les mis en cause. Ensuite, comptez les victimes après 2022 qui ont aussi été des mis en cause en utilisant une jointure des deux tables.

**Indices** :
- Utilisez `pd.merge()` pour effectuer une jointure entre deux DataFrames.
- Utilisez `isin()` pour vérifier l'appartenance à un ensemble d'identifiants.

## Question 4 : Calculer la moyenne d'âge des victimes par sexe

**Objectif** : Calculer la moyenne d'âge des victimes en fonction de leur sexe.

**Tâche** : Écrivez une fonction `moyenne_age_par_sexe` qui prend un DataFrame et retourne la moyenne d'âge pour chaque sexe.

**Indices** :
- Utilisez `groupby()` pour regrouper les données par sexe.
- Utilisez `mean()` pour calculer la moyenne d'âge pour chaque groupe.

## Question 5 : Trouver les infractions les plus fréquentes

**Objectif** : Identifier les infractions les plus fréquentes commises par les mis en cause.

**Tâche** : Écrivez une fonction `infractions_frequentes` qui prend un DataFrame et retourne les cinq infractions les plus fréquentes.

**Indices** :
- Utilisez `value_counts()` pour compter les occurrences de chaque infraction.
- Utilisez `head()` pour obtenir les cinq premières infractions les plus fréquentes.

## Question 6 : Analyser les infractions par région

**Objectif** : Analyser la distribution des infractions par région.

**Tâche** : Écrivez une fonction `infractions_par_region` qui prend les DataFrames des mis en cause et des villes, et retourne le nombre d'infractions par région.

**Indices** :
- Utilisez `pd.merge()` pour joindre les DataFrames des mis en cause et des villes.
- Utilisez `groupby()` pour regrouper les données par région.
- Utilisez `size()` pour compter le nombre d'infractions par région.

# Questionnaire de Visualisation Graphique avec Python

## Question 1 : Représentation du nombre d'infractions par type dans le temps

**Objectif** : Créer un graphique montrant l'évolution du nombre d'infractions par type au fil du temps.

**Tâche** : Utilisez un graphique en aires empilées pour montrer comment le nombre de chaque type d'infraction a évolué au fil des années.

**Indices** :
- Utilisez `groupby` pour regrouper les données par année et par type d'infraction.
- Utilisez `unstack` pour réorganiser les données pour le graphique.
- Utilisez `matplotlib` ou `seaborn` pour créer le graphique en aires empilées.

## Question 2 : Représentation du nombre de victimes par département en moyenne par an

**Objectif** : Créer une carte de France montrant le nombre moyen de victimes par département et par an entre deux années spécifiques.

**Tâche** : Utilisez une carte choroplèthe pour visualiser ces données.

**Indices** :
- Calculez le nombre moyen de victimes par département et par an.
- Utilisez une bibliothèque comme `geopandas` pour manipuler les données géographiques.
- Utilisez `matplotlib` pour tracer la carte choroplèthe.

## Question 3 : Répartition des âges des victimes et de leurs agresseurs

**Objectif** : Créer un graphique montrant la répartition des âges des victimes et des agresseurs.

**Tâche** : Utilisez un histogramme ou un graphique de densité pour comparer la distribution des âges entre les victimes et les agresseurs.

**Indices** :
- Utilisez `seaborn` pour créer des graphiques de densité ou des histogrammes.
- Superposez les graphiques pour une comparaison facile.

## Question 4 : Évolution du nombre total d'infractions par région

**Objectif** : Créer un graphique montrant l'évolution du nombre total d'infractions par région au fil du temps.

**Tâche** : Utilisez un graphique en lignes pour montrer cette évolution pour chaque région.

**Indices** :
- Utilisez `groupby` pour regrouper les données par année et par région.
- Utilisez `matplotlib` pour tracer un graphique en lignes.

## Question 5 : Comparaison du nombre de victimes et d'infractions par mois

**Objectif** : Créer un graphique montrant le nombre de victimes et d'infractions par mois pour une année spécifique.

**Tâche** : Utilisez un graphique à barres groupées pour comparer ces deux ensembles de données.

**Indices** :
- Utilisez `groupby` pour regrouper les données par mois.
- Utilisez `matplotlib` pour créer un graphique à barres groupées.


# Exercice d'Analyse Avancée de Données avec Python

## Question 1 : Déterminer le nombre optimal de catégories pour l'âge

**Objectif** : Utiliser l'Analyse en Composantes Principales (ACP) et la Classification Ascendante Hiérarchique (CAH) pour déterminer le nombre optimal de catégories pour l'âge des victimes et des mis en cause.

**Tâche** : Appliquez l'ACP et la CAH sur les données d'âge des victimes et des mis en cause pour déterminer le nombre optimal de catégories.

**Indices** :
- Utilisez `StandardScaler` pour normaliser les données avant l'ACP.
- Utilisez `PCA` de `sklearn.decomposition` pour l'Analyse en Composantes Principales.
- Utilisez `linkage` et `dendrogram` de `scipy.cluster.hierarchy` pour la Classification Ascendante Hiérarchique.

## Question 2 : Regrouper les victimes par âge en utilisant k-NN

**Objectif** : Regrouper les victimes en catégories d'âge en utilisant la méthode des k-plus proches voisins (k-NN).

**Tâche** : Ajoutez une colonne `categorie_age_knn` au DataFrame des victimes en utilisant l'algorithme k-NN pour regrouper les âges.

**Indices** :
- Utilisez `KMeans` de `sklearn.cluster` pour déterminer les catégories d'âge.
- Ajoutez les résultats comme une nouvelle colonne dans le DataFrame des victimes.
- Sauvegardez les résultats dans un fichier Parquet.

## Question 3 : Prédire le nombre de victimes par département pour les années à venir

**Objectif** : Utiliser un modèle de séries temporelles pour prédire le nombre de victimes et les départements concernés pour les années à venir.

**Tâche** : Prédisez le nombre de victimes pour les 5 prochaines années et identifiez les départements concernés.

**Indices** :
- Utilisez `ARIMA` de `statsmodels.tsa.arima.model` pour la prédiction des séries temporelles.
- Regroupez les données par année et département avant d'appliquer le modèle.
- Utilisez `forecast` pour prédire les valeurs futures.

# Exercice d'Analyse de Données de Décisions de Justice

## Question 1 : Lire et afficher les premières décisions

**Objectif** : Lire le fichier JSON et afficher les premières décisions.

**Tâche** : Écrivez un script Python pour lire le fichier JSON et afficher les cinq premières décisions.

**Indices** :
- Utilisez la bibliothèque `json` pour lire le fichier JSON.
- Utilisez `pandas` pour convertir les données en DataFrame et afficher les premières lignes.

## Question 2 : Statistiques descriptives

**Objectif** : Calculer des statistiques descriptives sur les décisions.

**Tâche** : Calculez et affichez des statistiques descriptives pour les décisions, telles que le nombre total de décisions, le nombre de types de recours uniques, etc.

**Indices** :
- Utilisez la méthode `describe()` de `pandas` pour obtenir des statistiques descriptives.
- Utilisez `value_counts()` pour compter les occurrences uniques de certaines colonnes.

## Question 3 : Compter les décisions par type de recours

**Objectif** : Compter le nombre de décisions par type de recours.

**Tâche** : Écrivez un script pour compter et afficher le nombre de décisions pour chaque type de recours.

**Indices** :
- Utilisez `value_counts()` sur la colonne appropriée pour compter les occurrences de chaque type de recours.

## Question 4 : Compter les décisions par année

**Objectif** : Compter le nombre de décisions par année.

**Tâche** : Écrivez un script pour compter et afficher le nombre de décisions pour chaque année.

**Indices** :
- Convertissez la colonne de date en type datetime.
- Utilisez `dt.year` pour extraire l'année et `value_counts()` pour compter les occurrences par année.

## Question 5 : Analyser les solutions des décisions

**Objectif** : Analyser les solutions des décisions.

**Tâche** : Écrivez un script pour compter et afficher le nombre de décisions pour chaque solution.

**Indices** :
- Utilisez `value_counts()` sur la colonne des solutions pour compter les occurrences de chaque solution.
