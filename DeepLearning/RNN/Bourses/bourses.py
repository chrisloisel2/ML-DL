import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
nombre_de_jours = 365
prix_initial = 100.0

tendance_marche = np.linspace(0, 10, nombre_de_jours) + prix_initial

volatilite = np.random.normal(0, 2, nombre_de_jours)

prix = tendance_marche + volatilite

prix_ouverture = prix + np.random.normal(0, 1, nombre_de_jours)
prix_haut = prix + np.random.normal(0, 1.5, nombre_de_jours)
prix_bas = prix - np.random.normal(0, 1.5, nombre_de_jours)
prix_cloture = prix + np.random.normal(0, 1, nombre_de_jours)

volume = np.random.randint(100000, 500000, nombre_de_jours)

dates = pd.date_range(start=datetime.today().strftime('%Y-%m-%d'), periods=nombre_de_jours, freq='D')
data = {
    'Date': dates,
    'Ouverture': prix_ouverture,
    'Haut': prix_haut,
    'Bas': prix_bas,
    'Cloture': prix_cloture,
    'Volume': volume
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

print(df.head())

df.to_csv('dataset_bourse_simule.csv')

sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))
plt.plot(df['Cloture'], label='Prix de clôture')
plt.title('Prix de clôture de l\'action sur une année')
plt.xlabel('Date')
plt.ylabel('Prix')
plt.legend()
plt.show()

