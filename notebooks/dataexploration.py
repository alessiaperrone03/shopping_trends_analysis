import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Librerie importate con successo!")

# Carica il dataset
file_path = 'data/shopping_trends.csv'
df = pd.read_csv(file_path)

# Visualizza le prime righe
print(df.head())

# Dimensioni del dataset
print("Dimensioni del dataset:", df.shape)

# Tipi di dati
print("Tipi di dati:\n", df.dtypes)

# Colonne e statistiche iniziali
print("Informazioni generali:")
print(df.info())

# Riepilogo statistico delle colonne numeriche
print("Statistiche descrittive:")
print(df.describe())

print("Dati mancanti per colonna:\n", df.isnull().sum())
print("Righe duplicate:", df.duplicated().sum())
for col in df.columns:
    print(f"{col}: {df[col].nunique()} valori unici")

import matplotlib.pyplot as plt
import seaborn as sns

# Istogrammi
df.hist(figsize=(12, 8))
plt.show()

# Boxplot per identificare outlier
sns.boxplot(data=df)
plt.show()


for col in ['colonna_categorica']:
    print(df[col].value_counts())
    df[col].value_counts().plot(kind='bar')
    plt.title(f"Distribuzione di {col}")
    plt.show()


# Matrice di correlazione
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Matrice di correlazione")
plt.show()

sns.pairplot(df, diag_kind='kde')
plt.show()

