import pandas as pd

# Charger les données
victimes_df = pd.read_parquet('victimes.parquet')
mis_en_cause_df = pd.read_parquet('mis_en_cause.parquet')
cities_df = pd.read_parquet('cities.parquet')

# Question 1
def compte_victimes(df, annee_min, annee_max):
    victimes_periode = df[(df['Date du fait'].dt.year >= annee_min) & (df['Date du fait'].dt.year <= annee_max)]
    return len(victimes_periode)

nombre_victimes = compte_victimes(victimes_df, 2022, 2023)
print(f"Nombre de victimes entre 2022 et 2023 : {nombre_victimes}")

# Question 2
def compte_victimes(df, annee_min=None, annee_max=None, sexe_victime=None):
    victimes_filtrees = df
    if annee_min is not None:
        victimes_filtrees = victimes_filtrees[victimes_filtrees['Date du fait'].dt.year >= annee_min]
    if annee_max is not None:
        victimes_filtrees = victimes_filtrees[victimes_filtrees['Date du fait'].dt.year <= annee_max]
    if sexe_victime is not None:
        victimes_filtrees = victimes_filtrees[victimes_filtrees['Sexe'] == sexe_victime]
    return len(victimes_filtrees)

nombre_victimes_femmes = compte_victimes(victimes_df, annee_min=2022, sexe_victime='Femme')
print(f"Nombre de victimes après 2022 qui sont des femmes : {nombre_victimes_femmes}")

# Question 3
def compte_mis_en_cause(df, annee_min=None, annee_max=None):
    mis_en_cause_filtrees = df
    if annee_min is not None:
        mis_en_cause_filtrees = mis_en_cause_filtrees[mis_en_cause_filtrees['Date du fait'].dt.year >= annee_min]
    if annee_max is not None:
        mis_en_cause_filtrees = mis_en_cause_filtrees[mis_en_cause_filtrees['Date du fait'].dt.year <= annee_max]
    return len(mis_en_cause_filtrees)

victimes_apres_2022 = victimes_df[victimes_df['Date du fait'].dt.year > 2022]
mis_en_cause_avant_victimes = mis_en_cause_df[mis_en_cause_df['Identifiant national unique'].isin(victimes_apres_2022['Identifiant national unique'])]
nombre_victimes_et_mis_en_cause = len(mis_en_cause_avant_victimes)

victimes_et_mis_en_cause = pd.merge(victimes_apres_2022, mis_en_cause_df, on='Identifiant national unique', how='inner')
nombre_victimes_et_mis_en_cause_jointure = len(victimes_et_mis_en_cause)

print(f"Nombre de victimes après 2022 qui ont aussi été des mis en cause (première méthode) : {nombre_victimes_et_mis_en_cause}")
print(f"Nombre de victimes après 2022 qui ont aussi été des mis en cause (deuxième méthode) : {nombre_victimes_et_mis_en_cause_jointure}")

# Question 4
def moyenne_age_par_sexe(df):
    return df.groupby('Sexe')['Age'].mean()

moyenne_age = moyenne_age_par_sexe(victimes_df)
print("Moyenne d'âge des victimes par sexe:")
print(moyenne_age)

# Question 5
def infractions_frequentes(df):
    return df['Fait commis'].value_counts().head(5)

infractions_freq = infractions_frequentes(mis_en_cause_df)
print("Les cinq infractions les plus fréquentes:")
print(infractions_freq)

# Question 6
def infractions_par_region(mis_en_cause_df, cities_df):
    mis_en_cause_et_villes = pd.merge(mis_en_cause_df, cities_df, left_on='Lieu du fait', right_on='Ville', how='left')
    return mis_en_cause_et_villes.groupby('Région').size()

infractions_region = infractions_par_region(mis_en_cause_df, cities_df)
print("Nombre d'infractions par région:")
print(infractions_region)
