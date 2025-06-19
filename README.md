# Stage-seconde

Petits exercices pour les stagiaires de passage au ministère de l'intérieur

## Installations requises

```bash
pip install pyarrow
pip install Faker
```

## Pour générer le data

```bash
# générer les infractions et vicimes
python scripts/generateur_donnees_simples.py
# générer les procédures
python scripts/generateur_procedures.py
# Web scraper les décisions de justice publiques
python scripts/generateur_donnees_simples.py
```

## Pour lancer les corrections:

```bash
# réponses première partie
python exercice/réponses_analyses_simples.py
# réponses deuxième partie
python exercice/réponses_graphiques.py
# réponses troisième partie
python exercice/réponses_analyses_avancées.py
# réponses quatrième partie
python exercice/réponses_open_data.py
```
