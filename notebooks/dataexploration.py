# Import libraries / Importa le librerie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully! / Librerie importate con successo!")

# Load the dataset / Carica il dataset
file_path = '/Users/alessiaperrone/Documents/shopping_trends_analysis_project/shopping_trends_analysis/data/shopping_trends.csv'
df = pd.read_csv(file_path)

# Display the first rows of the dataset / Visualizza le prime righe del dataset
print("First rows of the dataset: / Prime righe del dataset:")
print(df.head())

# Dataset dimensions / Dimensioni del dataset
print("Dataset dimensions: / Dimensioni del dataset:", df.shape)

# Data types of each column / Tipi di dati delle colonne
print("Data types: / Tipi di dati:\n", df.dtypes)

# General information about the dataset / Informazioni generali sul dataset
print("General information: / Informazioni generali:")
print(df.info())

# Statistical summary of numerical columns / Statistiche descrittive delle colonne numeriche
print("Statistical summary: / Riepilogo statistico:")
print(df.describe())

# Missing values and duplicates / Valori mancanti e duplicati
print("Missing values per column: / Valori mancanti per colonna:\n", df.isnull().sum())
print("Duplicate rows: / Righe duplicate:", df.duplicated().sum())

# Unique values in each column / Valori unici per colonna
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values / valori unici")

# Histograms of numerical columns / Istogrammi delle colonne numeriche
df.hist(figsize=(14, 10), color='skyblue', edgecolor='black')
plt.suptitle("Histograms of numerical columns / Istogrammi delle colonne numeriche", fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

# Boxplot to identify outliers / Boxplot per identificare outlier
plt.figure(figsize=(14, 8))
sns.boxplot(data=df, palette='pastel')
plt.title("Boxplot to identify outliers / Boxplot per identificare outlier", fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.show()

# Select categorical columns / Seleziona le colonne categoriche
categorical_columns = df.select_dtypes(include=['object', 'category']).columns
print("Categorical columns: / Colonne categoriche:", categorical_columns)


# Value counts and bar plots for categorical columns / Conteggio valori e grafici a barre per colonne categoriche
for column in categorical_columns:
    print(f"Value counts for {column}: / Conteggio valori per {column}:")
    print(df[column].value_counts())
    
    plt.figure(figsize=(12, 8))
    sns.countplot(data=df, x=column, hue=column, dodge=False, order=df[column].value_counts().index, legend=False)
    plt.title(f"Distribution of {column} / Distribuzione di {column}", fontsize=16)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()


# Select numerical columns for correlation / Seleziona colonne numeriche per la correlazione
numeric_df = df.select_dtypes(include=[np.number])

# Correlation matrix / Matrice di correlazione
correlation = numeric_df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix / Matrice di correlazione", fontsize=16)
plt.show()

# Pairplot of numerical columns / Pairplot delle colonne numeriche
sns.pairplot(numeric_df, diag_kind='kde', corner=True, plot_kws={'alpha': 0.5}, height=2.5)
plt.suptitle("Pairplot of Numerical Columns / Pairplot delle colonne numeriche", y=1.02, fontsize=16)
plt.show()


