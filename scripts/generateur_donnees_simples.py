import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker('fr_FR')

# List of possible offenses and other data
possible_offenses = [
    "Vol à l'étalage", "Conduite sous influence", "Vandalisme", "Fraude", "Agression",
    "Cambriolage", "Escroquerie", "Usage de stupéfiants", "Délit de fuite", "Harcèlement",
    "Menaces", "Recel", "Faux et usage de faux", "Violences volontaires", "Trafic de drogue",
    "Prise illégale d'intérêt", "Atteinte à la vie privée", "Diffamation", "Injures", "Travail dissimulé",
    "Contrefaçon", "Blanchiment d'argent", "Corruption", "Violation de domicile", "Port illégal d'arme",
    "Violences conjugales", "Violences sur mineur", "Non-respect du code de la route", "Trafic d'influence",
    "Cybercriminalité"
]

sexes = ['Homme', 'Femme', 'Autre']
professions = [
    "Étudiant", "Enseignant", "Ingénieur", "Médecin", "Artisan", "Commerçant", "Cadre",
    "Ouvrier", "Retraité", "Sans emploi", "Technicien", "Profession libérale"
]

# Sample data for cities, departments, and regions
cities_data = [
    {"Ville": "Paris", "Département": "Paris", "Région": "Île-de-France"},
    {"Ville": "Boulogne-Billancourt", "Département": "Hauts-de-Seine", "Région": "Île-de-France"},
    {"Ville": "Marseille", "Département": "Bouches-du-Rhône", "Région": "Provence-Alpes-Côte d'Azur"},
    {"Ville": "Nice", "Département": "Alpes-Maritimes", "Région": "Provence-Alpes-Côte d'Azur"},
    {"Ville": "Lyon", "Département": "Rhône", "Région": "Auvergne-Rhône-Alpes"},
    {"Ville": "Saint-Étienne", "Département": "Loire", "Région": "Auvergne-Rhône-Alpes"},
    {"Ville": "Toulouse", "Département": "Haute-Garonne", "Région": "Occitanie"},
    {"Ville": "Montpellier", "Département": "Hérault", "Région": "Occitanie"},
    {"Ville": "Nantes", "Département": "Loire-Atlantique", "Région": "Pays de la Loire"},
    {"Ville": "Angers", "Département": "Maine-et-Loire", "Région": "Pays de la Loire"},
    {"Ville": "Bordeaux", "Département": "Gironde", "Région": "Nouvelle-Aquitaine"},
    {"Ville": "Limoges", "Département": "Haute-Vienne", "Région": "Nouvelle-Aquitaine"},
    {"Ville": "Lille", "Département": "Nord", "Région": "Hauts-de-France"},
    {"Ville": "Amiens", "Département": "Somme", "Région": "Hauts-de-France"},
    {"Ville": "Strasbourg", "Département": "Bas-Rhin", "Région": "Grand Est"},
    {"Ville": "Reims", "Département": "Marne", "Région": "Grand Est"},
    {"Ville": "Rennes", "Département": "Ille-et-Vilaine", "Région": "Bretagne"},
    {"Ville": "Brest", "Département": "Finistère", "Région": "Bretagne"},
    {"Ville": "Dijon", "Département": "Côte-d'Or", "Région": "Bourgogne-Franche-Comté"},
    {"Ville": "Besançon", "Département": "Doubs", "Région": "Bourgogne-Franche-Comté"},
    {"Ville": "Orléans", "Département": "Loiret", "Région": "Centre-Val de Loire"},
    {"Ville": "Tours", "Département": "Indre-et-Loire", "Région": "Centre-Val de Loire"},
    {"Ville": "Clermont-Ferrand", "Département": "Puy-de-Dôme", "Région": "Auvergne-Rhône-Alpes"},
    {"Ville": "Grenoble", "Département": "Isère", "Région": "Auvergne-Rhône-Alpes"},
    {"Ville": "Rouen", "Département": "Seine-Maritime", "Région": "Normandie"},
    {"Ville": "Caen", "Département": "Calvados", "Région": "Normandie"},
    {"Ville": "Toulon", "Département": "Var", "Région": "Provence-Alpes-Côte d'Azur"},
    {"Ville": "Aix-en-Provence", "Département": "Bouches-du-Rhône", "Région": "Provence-Alpes-Côte d'Azur"},
    {"Ville": "Le Havre", "Département": "Seine-Maritime", "Région": "Normandie"},
    {"Ville": "Saint-Denis", "Département": "Seine-Saint-Denis", "Région": "Île-de-France"}
]

def generate_data(num_records):
    mis_en_cause_data = []
    victimes_data = []

    for _ in range(num_records):
        id_unique = fake.unique.random_number(digits=8)
        age = random.randint(18, 80)
        date_naissance = fake.date_of_birth(minimum_age=age, maximum_age=age)
        sexe = random.choice(sexes)
        profession = random.choice(professions)
        nationalite = fake.country()
        situation_familiale = random.choice(['Célibataire', 'Marié', 'Divorcé', 'Veuf', 'Union libre'])
        niveau_etude = random.choice(['Aucun diplôme', 'BEP/CAP', 'Baccalauréat', 'Licence', 'Master', 'Doctorat'])

        # Randomly select a city from the predefined list
        city_info = random.choice(cities_data)
        lieu_naissance = city_info["Ville"]
        lieu_fait = random.choice(cities_data)["Ville"]

        mis_en_cause_data.append({
            "Identifiant national unique": id_unique,
            "Age": age,
            "Sexe": sexe,
            "Date de naissance": date_naissance,
            "Lieu de naissance": lieu_naissance,
            "Profession": profession,
            "Nationalité": nationalite,
            "Situation familiale": situation_familiale,
            "Niveau d'étude": niveau_etude,
            "Date du fait": fake.date_between(start_date='-5y', end_date='today'),
            "Lieu du fait": lieu_fait,
            "Fait commis": random.choice(possible_offenses)
        })

        id_unique = fake.unique.random_number(digits=8)
        age = random.randint(1, 90)
        date_naissance = fake.date_of_birth(minimum_age=age, maximum_age=age)
        sexe = random.choice(sexes)
        profession = random.choice(professions)
        nationalite = fake.country()
        situation_familiale = random.choice(['Célibataire', 'Marié', 'Divorcé', 'Veuf', 'Union libre'])
        niveau_etude = random.choice(['Aucun diplôme', 'BEP/CAP', 'Baccalauréat', 'Licence', 'Master', 'Doctorat'])

        # Randomly select a city from the predefined list
        city_info = random.choice(cities_data)
        lieu_naissance = city_info["Ville"]
        lieu_fait = random.choice(cities_data)["Ville"]

        victimes_data.append({
            "Identifiant national unique": id_unique,
            "Age": age,
            "Sexe": sexe,
            "Date de naissance": date_naissance,
            "Lieu de naissance": lieu_naissance,
            "Profession": profession,
            "Nationalité": nationalite,
            "Situation familiale": situation_familiale,
            "Niveau d'étude": niveau_etude,
            "Date du fait": fake.date_between(start_date='-5y', end_date='today'),
            "Lieu du fait": lieu_fait
        })

    mis_en_cause_df = pd.DataFrame(mis_en_cause_data)
    victimes_df = pd.DataFrame(victimes_data)
    cities_df = pd.DataFrame(cities_data)

    return mis_en_cause_df, victimes_df, cities_df

def save_to_parquet(mis_en_cause_df, victimes_df, cities_df, mis_en_cause_file, victimes_file, cities_file):
    mis_en_cause_df.to_parquet(mis_en_cause_file, engine='pyarrow')
    victimes_df.to_parquet(victimes_file, engine='pyarrow')
    cities_df.to_parquet(cities_file, engine='pyarrow')

# Generate data with 1500 records
mis_en_cause_df, victimes_df, cities_df = generate_data(1500)

# Save to Parquet files
mis_en_cause_file = 'data/mis_en_cause.parquet'
victimes_file = 'data/victimes.parquet'
cities_file = 'data/cities.parquet'
save_to_parquet(mis_en_cause_df, victimes_df, cities_df, mis_en_cause_file, victimes_file, cities_file)
