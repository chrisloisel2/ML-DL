import pandas as pd
import numpy as np

# Définition des maladies et de leurs symptômes associés
maladies = ['Grippe', 'Rhume', 'Gastro-entérite', 'Varicelle', 'Rougeole', 'Malaria', 'Dengue', 'COVID-19', 'Angine', 'Bronchite']
symptomes = [
    'Fièvre', 'Toux', 'Maux de tête', 'Douleurs musculaires', 'Congestion nasale', 'Nausées', 'Diarrhée', 'Éruptions cutanées',
    'Douleurs articulaires', 'Fatigue', 'Difficultés respiratoires', 'Mal de gorge'
]

# Mapping des maladies à leurs symptômes principaux (pour garantir leur présence)
symptomes_par_maladie = {
    'Grippe': ['Fièvre', 'Toux', 'Maux de tête', 'Douleurs musculaires'],
    'Rhume': ['Toux', 'Congestion nasale'],
    'Gastro-entérite': ['Nausées', 'Diarrhée'],
    'Varicelle': ['Fièvre', 'Éruptions cutanées'],
    'Rougeole': ['Fièvre', 'Éruptions cutanées', 'Toux'],
    'Malaria': ['Fièvre', 'Douleurs musculaires', 'Fatigue'],
    'Dengue': ['Fièvre', 'Douleurs articulaires', 'Nausées'],
    'COVID-19': ['Fièvre', 'Toux', 'Difficultés respiratoires'],
    'Angine': ['Fièvre', 'Mal de gorge'],
    'Bronchite': ['Toux', 'Douleurs musculaires', 'Difficultés respiratoires']
}

# Génération des données
data = []

for maladie, symptomes_principaux in symptomes_par_maladie.items():
    for _ in range(5000):  # 5000 instances par maladie pour atteindre 50 000 au total
        # Génération des symptômes
        symptomes_maladie = [1 if s in symptomes_principaux else 0 for s in symptomes]
        data.append([maladie] + symptomes_maladie)


# Création du DataFrame
df = pd.DataFrame(data, columns=['Maladie'] + symptomes)

# Shuffle des lignes
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('maladies.csv', index=False)

# Affichage des premières lignes pour vérification
print(df.head())

# Informations sur le DataFrame
print(f"Taille du dataset : {df.shape}")
