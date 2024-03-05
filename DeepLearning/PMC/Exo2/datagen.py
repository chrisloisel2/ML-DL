import numpy as np
import pandas as pd

## Nous avons une tourelle automatique qui tire des projectiles sur des cibles.
## Nous devons générer un dataset pour prédire la hauteur du tir en fonctions des paramètres suivants:
distance = np.random.uniform(50, 500, 50000)
gravitational_force = np.random.uniform(0.5, 2.0, 50000)
wind_speed = np.random.uniform(0, 20, 50000)
wind_direction = np.random.uniform(0, 360, 50000)
projectile_mass = np.random.uniform(0.1, 10, 50000)

## La hauteur du tir est donnée par la formule suivante:
hauteur_tir = 0.001 * distance**2 + 5 * gravitational_force**3 - 0.1 * wind_speed + 0.01 * wind_direction + 0.5 * projectile_mass

## Création du DataFrame
data = pd.DataFrame({
	'distance': distance,
	'gravitational_force': gravitational_force,
	'wind_speed': wind_speed,
	'wind_direction': wind_direction,
	'projectile_mass': projectile_mass,
	'hauteur_tir': hauteur_tir
})

# Génération de données linéaires
np.random.seed(42)  # Pour la reproductibilité

# Affichage des premières lignes du DataFrame
data.head()
data.to_csv('balistic.csv', index=False)
