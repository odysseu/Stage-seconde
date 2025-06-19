import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point

# Charger les données
victimes_df = pd.read_parquet('victimes.parquet')
mis_en_cause_df = pd.read_parquet('mis_en_cause.parquet')
cities_df = pd.read_parquet('cities.parquet')

# Question 1: Représentation du nombre d'infractions par type dans le temps
def plot_infractions_par_type_dans_le_temps(df):
    df['Année'] = df['Date du fait'].dt.year
    infractions_par_annee_type = df.groupby(['Année', 'Fait commis']).size().unstack()
    infractions_par_annee_type.plot(kind='area', stacked=True, figsize=(12, 6))
    plt.title('Évolution du nombre d\'infractions par type dans le temps')
    plt.xlabel('Année')
    plt.ylabel('Nombre d\'infractions')
    plt.show()

plot_infractions_par_type_dans_le_temps(mis_en_cause_df)

# Question 2: Représentation du nombre de victimes par département en moyenne par an
def plot_victimes_par_departement(df, annee_min, annee_max):
    df['Année'] = df['Date du fait'].dt.year
    victimes_departement_annee = df[df['Année'].between(annee_min, annee_max)].groupby(['Lieu du fait', 'Année']).size().mean(level=0)
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    france = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    # Note: This is a simplified example; you'll need actual shapefiles for French departments.
    # Here, we assume `victimes_departement_annee` is a GeoDataFrame with department geometries.
    victimes_departement_annee.plot(ax=ax, legend=True)
    plt.title(f'Nombre moyen de victimes par département entre {annee_min} et {annee_max}')
    plt.show()

plot_victimes_par_departement(victimes_df, 2020, 2023)

# Question 3: Répartition des âges des victimes et de leurs agresseurs
def plot_repartition_ages(df_victimes, df_agresseurs):
    plt.figure(figsize=(12, 6))
    sns.kdeplot(df_victimes['Age'], label='Victimes', shade=True)
    sns.kdeplot(df_agresseurs['Age'], label='Agresseurs', shade=True)
    plt.title('Répartition des âges des victimes et de leurs agresseurs')
    plt.xlabel('Âge')
    plt.ylabel('Densité')
    plt.legend()
    plt.show()

plot_repartition_ages(victimes_df, mis_en_cause_df)

# Question 4: Évolution du nombre total d'infractions par région
def plot_infractions_par_region_dans_le_temps(df, cities_df):
    df_merged = pd.merge(df, cities_df, left_on='Lieu du fait', right_on='Ville')
    infractions_par_annee_region = df_merged.groupby(['Année', 'Région']).size().unstack()
    infractions_par_annee_region.plot(figsize=(12, 6))
    plt.title('Évolution du nombre total d\'infractions par région')
    plt.xlabel('Année')
    plt.ylabel('Nombre d\'infractions')
    plt.show()

mis_en_cause_df['Année'] = mis_en_cause_df['Date du fait'].dt.year
plot_infractions_par_region_dans_le_temps(mis_en_cause_df, cities_df)

# Question 5: Comparaison du nombre de victimes et d'infractions par mois
def plot_comparaison_victimes_infractions_par_mois(df_victimes, df_infractions, annee):
    df_victimes['Mois'] = df_victimes['Date du fait'].dt.month
    df_infractions['Mois'] = df_infractions['Date du fait'].dt.month
    victimes_par_mois = df_victimes[df_victimes['Date du fait'].dt.year == annee].groupby('Mois').size()
    infractions_par_mois = df_infractions[df_infractions['Date du fait'].dt.year == annee].groupby('Mois').size()
    df_comparaison = pd.DataFrame({'Victimes': victimes_par_mois, 'Infractions': infractions_par_mois})
    df_comparaison.plot(kind='bar', figsize=(12, 6))
    plt.title(f'Comparaison du nombre de victimes et d\'infractions par mois pour {annee}')
    plt.xlabel('Mois')
    plt.ylabel('Nombre')
    plt.show()

plot_comparaison_victimes_infractions_par_mois(victimes_df, mis_en_cause_df, 2022)
