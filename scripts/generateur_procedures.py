import json
import random
from faker import Faker

# Initialize Faker for generating fake text
fake = Faker('fr_FR')

# List of possible offenses
possible_offenses = [
    "Vol à l'étalage", "Conduite sous influence", "Vandalisme", "Fraude", "Agression",
    "Cambriolage", "Escroquerie", "Usage de stupéfiants", "Délit de fuite", "Harcèlement",
    "Menaces", "Recel", "Faux et usage de faux", "Violences volontaires", "Trafic de drogue",
    "Prise illégale d'intérêt", "Atteinte à la vie privée", "Diffamation", "Injures", "Travail dissimulé",
    "Contrefaçon", "Blanchiment d'argent", "Corruption", "Violation de domicile", "Port illégal d'arme",
    "Violences conjugales", "Violences sur mineur", "Non-respect du code de la route", "Trafic d'influence",
    "Cybercriminalité"
]

# Generate 1000 short and varied summaries with associated offenses
summaries_list = []

for _ in range(1000):
    # Randomly select one or two offenses
    offenses = random.sample(possible_offenses, k=random.randint(1, 2))

    # Generate a short summary
    summary = {
        "Résumé": fake.sentence(nb_words=30) + f" L'infraction commise inclut {', '.join(offenses)}.",
        "Infractions": offenses
    }

    summaries_list.append(summary)

# Save the summaries to a JSON file
json_file_path = 'data/short_procedure_summaries_with_infractions.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(summaries_list, json_file, ensure_ascii=False, indent=4)

print(f"Les résumés ont été sauvegardés dans le fichier : {json_file_path}")