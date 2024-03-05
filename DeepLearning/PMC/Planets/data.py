import pandas as pd
import numpy as np

# Fixons le germe aléatoire pour la reproductibilité
np.random.seed(42)

n_planets = 500000

# Génération des caractéristiques
names = [f"Planet_{i}" for i in range(n_planets)]
num_moons = np.random.randint(0, 10, n_planets)
minerals = np.random.randint(0, 1024, n_planets)
gravity = np.random.uniform(0.1, 3.0, n_planets)
sunlight_hours = np.random.uniform(0, 24, n_planets)
temperature = np.random.uniform(-100, 100, n_planets)
rotation_time = np.random.uniform(10, 100, n_planets)
water_presence = np.random.randint(0, 2, n_planets)

# Calcul de la colonne 'Colonisable' basé sur des règles prédéfinies
colonisable = ((gravity > 0.7) & (gravity < 2.3) &
               (temperature > -20) & (temperature < 50) &
               (water_presence == 1) &
               (sunlight_hours > 2) & (sunlight_hours < 16) &
               ((minerals & 1) == 1)).astype(int)

# Création du DataFrame
planets_df = pd.DataFrame({
    'Name': names,
    'Num_Moons': num_moons,
    'Minerals': minerals,
    'Gravity': gravity,
    'Sunlight_Hours': sunlight_hours,
    'Temperature': temperature,
    'Rotation_Time': rotation_time,
    'Water_Presence': water_presence,
    'Colonisable': colonisable
})

# Affichage des premières lignes pour vérification
print(planets_df.head())

# Shuffling des données
planets_df = planets_df.sample(frac=1).reset_index(drop=True)

print(planets_df['Colonisable'].value_counts())

# # Suréchantillonnage des données pour la classe minoritaire
# minority_class = planets_df[planets_df['Colonisable'] == 1]
# oversampled = minority_class.sample(n=10000, replace=True)
# planets_df = pd.concat([planets_df, oversampled], ignore_index=True)


# Enregistrement du DataFrame dans un fichier CSV (optionnel)
planets_df.to_csv('planets_dataset.csv', index=False)
