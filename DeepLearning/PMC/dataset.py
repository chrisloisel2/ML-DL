import numpy as np
import pandas as pd

def generate_dataset(n_samples=50000):
    # Générer des données aléatoires pour les caractéristiques
    Distance = np.random.uniform(50, 500, n_samples)  # Distance en millions de kilomètres
    Gravitational_Force = np.random.uniform(0.5, 2.0, n_samples)  # Force gravitationnelle en unités arbitraires
    Propulsion_Technology = np.random.randint(1, 4, n_samples)  # Technologie de propulsion (1 à 3)

    # Générer le temps de trajet en utilisant une fonction polynomiale des caractéristiques
    # Exemple de fonction polynomiale : Travel_Time = a*Distance^2 + b*Gravitational_Force^3 + c*Propulsion_Technology + d
    # où a, b, c, et d sont des coefficients arbitraires choisis pour l'exemple
    a, b, c, d = 0.001, 5, -10, 100  # Coefficients arbitraires
    Travel_Time = a * Distance**2 + b * Gravitational_Force**3 + c + d

    # Création d'un DataFrame
    df = pd.DataFrame({
        'Distance': Distance,
        'Gravitational_Force': Gravitational_Force,
        'Travel_Time': Travel_Time
    })

    return df

# Générer le dataset
dataset = generate_dataset()

dataset.to_csv('dataset.csv', index=False)

# Afficher les premières lignes du dataset pour vérifier
print(dataset.head())

# Utiliser seaborn pour visualiser les relations entre les caractéristiques et la variable cible
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(dataset)
plt.show()
# Output:
