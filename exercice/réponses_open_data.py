import json
import pandas as pd

json_path = 'data/decisions.json'
# Lire le fichier JSON
with open(json_path, 'r', encoding='utf-8') as json_file:
    decisions = json.load(json_file)

# Convertir les données en DataFrame pandas
df = pd.DataFrame(decisions)

# Question 1: Lire et afficher les premières décisions
print("Question 1: Lire et afficher les premières décisions")
print(df.head())

# Question 2: Statistiques descriptives
print("\nQuestion 2: Statistiques descriptives")
print(df.describe())
print("\nNombre de types de recours uniques :")
print(df['Type_Recours'].nunique())

# Question 3: Compter les décisions par type de recours
print("\nQuestion 3: Compter les décisions par type de recours")
type_recours_counts = df['Type_Recours'].value_counts()
print(type_recours_counts)

# Question 4: Compter les décisions par année
print("\nQuestion 4: Compter les décisions par année")
df['Date_Lecture'] = pd.to_datetime(df['Date_Lecture'], errors='coerce')
df['Année'] = df['Date_Lecture'].dt.year
annee_counts = df['Année'].value_counts().sort_index()
print(annee_counts)

# Question 5: Analyser les solutions des décisions
print("\nQuestion 5: Analyser les solutions des décisions")
solution_counts = df['Solution'].value_counts()
print(solution_counts)
