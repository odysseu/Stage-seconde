import requests
import zipfile
import io
import xml.etree.ElementTree as ET
import json
from datetime import datetime

json_path = 'data/decisions.json'

def get_zip_urls(start_year, end_year):
    zip_urls = []

    # Parcourir les années et les mois
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Formater le mois avec deux chiffres
            month_str = f"{month:02d}"

            # Construire l'URL
            url = f"https://opendata.justice-administrative.fr/DCE/{year}/{month_str}/CE_{year}{month_str}.zip"

            # Vérifier si l'URL est accessible
            response = requests.head(url)
            if response.status_code == 200:
                zip_urls.append(url)
                print(f"Found: {url}")
            else:
                print(f"Not found: {url}")

    return zip_urls

def append_decisions_to_json(new_decisions, json_file_path):
    try:
        # Lire les données existantes
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            existing_decisions = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_decisions = []

    # Ajouter les nouvelles décisions
    existing_decisions.extend(new_decisions)

    # Sauvegarder les décisions mises à jour
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(existing_decisions, json_file, ensure_ascii=False, indent=4)

# Définir la plage d'années à parcourir
start_year = 2019
end_year = datetime.now().year

# Récupérer les URLs des fichiers ZIP
zip_urls = get_zip_urls(start_year, end_year)
print(f"Total ZIP URLs found: {len(zip_urls)}")

# Parcourir les URLs des fichiers ZIP et extraire les décisions
for url in zip_urls:
    print(f"Processing: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
            decisions = []
            for zipinfo in thezip.infolist():
                with thezip.open(zipinfo) as file:
                    try:
                        tree = ET.parse(file)
                        root = tree.getroot()

                        identification = root.findtext(".//Identification", default="Non spécifié")
                        date_mise_jour = root.findtext(".//Date_Mise_Jour", default="Non spécifié")
                        code_juridiction = root.findtext(".//Code_Juridiction", default="Non spécifié")
                        nom_juridiction = root.findtext(".//Nom_Juridiction", default="Non spécifié")
                        numero_dossier = root.findtext(".//Numero_Dossier", default="Non spécifié")
                        date_lecture = root.findtext(".//Date_Lecture", default="Non spécifié")
                        numero_ecli = root.findtext(".//Numero_ECLI", default="Non spécifié")
                        type_decision = root.findtext(".//Type_Decision", default="Non spécifié")
                        type_recours = root.findtext(".//Type_Recours", default="Non spécifié")
                        code_publication = root.findtext(".//Code_Publication", default="Non spécifié")
                        solution = root.findtext(".//Solution", default="Non spécifié")
                        texte_integral = root.findtext(".//Texte_Integral", default="Non spécifié")

                        decision = {
                            "Identification": identification,
                            "Date_Mise_Jour": date_mise_jour,
                            "Code_Juridiction": code_juridiction,
                            "Nom_Juridiction": nom_juridiction,
                            "Numero_Dossier": numero_dossier,
                            "Date_Lecture": date_lecture,
                            "Numero_ECLI": numero_ecli,
                            "Type_Decision": type_decision,
                            "Type_Recours": type_recours,
                            "Code_Publication": code_publication,
                            "Solution": solution,
                            "Texte_Integral": texte_integral
                        }
                        decisions.append(decision)
                    except ET.ParseError:
                        print(f"Erreur lors de l'analyse du fichier XML : {zipinfo.filename}")
                    except Exception as e:
                        print(f"Erreur inattendue lors du traitement du fichier {zipinfo.filename}: {e}")

            # Ajouter les décisions au fichier JSON
            append_decisions_to_json(decisions, json_path)
    else:
        print(f"La requête a échoué avec le code d'état : {response.status_code}")

print(f"Les décisions ont été ajoutées au fichier {json_path}")
