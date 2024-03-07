import pandas as pd
import numpy as np

np.random.seed(42)
nombre_heures = 24 * 365
timestamps = pd.date_range(start='2023-01-01', periods=nombre_heures, freq='H')

amplitude_saisonnière = 10
température_moyenne = 15
températures = amplitude_saisonnière * np.sin(np.linspace(0, 2 * np.pi, nombre_heures)) + température_moyenne + np.random.normal(0, 2, nombre_heures)

df = pd.DataFrame({'Timestamp': timestamps, 'Température': températures})

print(df.head())

df.to_csv('donnees_temperature_simulees.csv', index=False)
