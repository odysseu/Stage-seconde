# Question 1: Déterminer le nombre optimal de catégories pour l'âge
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# Charger les données
victimes_df = pd.read_parquet('victimes.parquet')
mis_en_cause_df = pd.read_parquet('mis_en_cause.parquet')

def prepare_data_for_pca(df, age_column):
    data = df[[age_column]].dropna()
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    return data_scaled

def apply_pca(data_scaled):
    pca = PCA(n_components=1)
    principal_components = pca.fit_transform(data_scaled)
    return principal_components

def apply_hac(data_scaled):
    linked = linkage(data_scaled, method='ward')
    plt.figure(figsize=(10, 7))
    dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
    plt.title('Dendrogramme pour la CAH')
    plt.show()

victimes_age_data = prepare_data_for_pca(victimes_df, 'Age')
apply_pca(victimes_age_data)
apply_hac(victimes_age_data)

mis_en_cause_age_data = prepare_data_for_pca(mis_en_cause_df, 'Age')
apply_pca(mis_en_cause_age_data)
apply_hac(mis_en_cause_age_data)

# Question 2: Regrouper les victimes par âge en utilisant k-NN
from sklearn.cluster import KMeans

def categorize_age_knn(df, age_column, n_clusters):
    data = df[[age_column]].dropna()
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['categorie_age_knn'] = kmeans.fit_predict(data_scaled)

    return df

victimes_df = categorize_age_knn(victimes_df, 'Age', n_clusters=5)
victimes_df.to_parquet('victimes_with_categories.parquet', engine='pyarrow')

# Question 3: Prédire le nombre de victimes par département pour les années à venir
from statsmodels.tsa.arima.model import ARIMA

def prepare_data_for_prediction(df, date_column, department_column):
    df['Année'] = df[date_column].dt.year
    victims_per_year_department = df.groupby(['Année', department_column]).size().unstack(fill_value=0)
    return victims_per_year_department

def predict_victims(victims_per_year_department, n_years):
    predictions = {}
    for department in victims_per_year_department.columns:
        model = ARIMA(victims_per_year_department[department], order=(1, 1, 1))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=n_years)
        predictions[department] = forecast
    return pd.DataFrame(predictions)

victims_per_year_department = prepare_data_for_prediction(victimes_df, 'Date du fait', 'Lieu du fait')
predictions = predict_victims(victims_per_year_department, n_years=5)
print("Prédictions du nombre de victimes par département pour les 5 prochaines années:")
print(predictions)
