import numpy as np
import pandas as pd

np.random.seed(42)  # Pour la reproductibilité

x1 = np.random.uniform(40, 60, 100)  # Temps de possession varie de 40% à 60%
x2 = np.random.randint(1, 10, 100)   # Nombre de tirs cadrés varie de 1 à 10

a, b, c, d, e, f = 0.01, 0.02, 0.01, -0.5, 0.5, 2

buts = a*(x1**2) + b*(x2**2) + c*x1*x2 + d*x1 + e*x2 + f

buts += np.random.normal(0, 1, 100)

df_foot = pd.DataFrame({
    'Temps_de_possession': x1,
    'Tirs_cadrés': x2,
    'Buts_marqués': buts
})

df_foot.head()

df_foot.to_csv('football.csv', index=False)
