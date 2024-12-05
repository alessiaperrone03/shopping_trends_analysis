import os

# Stampa la directory corrente
print("Directory corrente:", os.getcwd())

# Verifica se il file esiste
file_path = 'data/shopping_trends.csv'
print("Il file esiste:", os.path.exists(file_path))
