# shopping_trends_analysis

Progetto 1: Analisi di un database e-commerce (SQL + Tableau)

Obiettivo:
Esplorare un database di e-commerce per ricavare insight utili sul comportamento dei clienti, sulle vendite e sulle performance dei prodotti. Creare una dashboard interattiva in Tableau per presentare i risultati.

# Insight da sviluppare

Vendite totali e trend temporali:
- Qual è il fatturato mensile/annuale?
- C'è una stagionalità evidente (es. aumento durante i saldi)?
Clienti più preziosi:
- Chi sono i top 10 clienti per fatturato totale?
- Qual è il valore medio di un cliente (Customer Lifetime Value)?
Performance dei prodotti:
- Quali sono i prodotti più venduti?
- Quali hanno generato il maggior fatturato?
Analisi geografica:
- Quali regioni/città performano meglio?
- Qual è il valore medio dell’ordine per area geografica?
Categorie di prodotti:
- Quali categorie generano il maggior numero di vendite?
- Esistono categorie con margini di profitto più alti?
Tasso di ritorno dei clienti:
- Quanti clienti ritornano a fare acquisti?
- Qual è la percentuale di ordini ricorrenti rispetto a quelli unici?


# Step dettagliati per SQL

1. Comprendere il database

Analizza la struttura del database, le tabelle disponibili e le loro relazioni (es. schema ER).
Tabelle tipiche potrebbero includere:
orders: Contiene gli ordini con informazioni su data, cliente e prodotto.
customers: Elenco dei clienti con dettagli personali e geografici.
products: Informazioni sui prodotti (nome, categoria, prezzo).
order_details: Dettagli degli ordini (quantità, prezzo unitario, ecc.).

2. Scrivere le query SQL 

Trend temporali delle vendite:
sql
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(order_amount) AS total_sales
FROM orders
GROUP BY month
ORDER BY month;


Top 10 clienti per fatturato:
sql
SELECT 
    c.customer_id, 
    c.customer_name, 
    SUM(o.order_amount) AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_revenue DESC
LIMIT 10;

Prodotti più venduti:
sql
SELECT 
    p.product_name, 
    COUNT(od.product_id) AS total_units_sold,
    SUM(od.quantity * od.unit_price) AS total_revenue
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_units_sold DESC
LIMIT 10;

Analisi geografica:
sql
SELECT 
    c.region, 
    SUM(o.order_amount) AS total_sales, 
    AVG(o.order_amount) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_sales DESC;

Ordini ricorrenti:
sql
SELECT 
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(order_id) - COUNT(DISTINCT order_id) AS recurring_orders
FROM orders
GROUP BY customer_id
HAVING recurring_orders > 0;


# Step dettagliati per Tableau

1. Preparazione del dataset

Esporta i risultati delle query SQL in un formato compatibile (CSV o direttamente connettiti al database).
Organizza i dati in tabelle separate per ciascun insight (es. vendite mensili, top clienti, ecc.).

2. Connessione a Tableau

Collega Tableau al tuo database SQL o importa i file CSV generati.
Verifica le connessioni tra le tabelle per garantire la corretta associazione dei dati.

3. Creazione della dashboard

Visualizzazioni principali:

- Grafico a linea: Visualizza il trend temporale delle vendite mensili.
- Bar chart: Mostra i prodotti più venduti.
- Heatmap geografica: Analizza le vendite per regione.
- Tabella dinamica: Elenca i top 10 clienti per fatturato.

Filtri interattivi:

- Aggiungi filtri per anno, regione, categoria di prodotto.
- Consenti agli utenti di selezionare una combinazione di filtri per esplorare i dati.

Dashboard layout: Inserisci una sezione iniziale con KPI chiave:
- Vendite totali.
- Numero di clienti unici.
- Valore medio dell’ordine.
  
Output finale:

Una dashboard interattiva pubblicata su Tableau Public che consente di esplorare i dati e rispondere a domande di business in modo visivo e dinamico.



Colonne principali
Customer ID: Identificativo unico del cliente.
Age: Età del cliente.
Gender: Genere del cliente.
Item Purchased: Prodotto acquistato.
Category: Categoria del prodotto (es. Clothing, Footwear).
Purchase Amount (USD): Importo dell'acquisto in dollari.
Location: Regione geografica del cliente.
Size, Color, Season: Dettagli del prodotto (taglia, colore, stagione).
Review Rating: Valutazione dell'acquisto (da 1 a 5 stelle).
Subscription Status: Stato di abbonamento del cliente (Yes/No).
Payment Method: Metodo di pagamento utilizzato.
Shipping Type: Tipo di spedizione scelta.
Discount Applied, Promo Code Used: Applicazione di sconti e codici promozionali.
Previous Purchases: Numero di acquisti precedenti del cliente.
Preferred Payment Method: Metodo di pagamento preferito.
Frequency of Purchases: Frequenza con cui il cliente effettua acquisti.
Step per l'analisi SQL e Tableau


1. Obiettivi e Insight da sviluppare
Trend delle vendite per stagione o periodo temporale.
Clienti con maggiore spesa totale: identificare i top spender.
Analisi geografica: Quali regioni generano maggior fatturato?
Performance delle categorie di prodotti: quali generano più vendite e recensioni migliori?
Frequenza di acquisto e fidelizzazione: analizzare il comportamento di ritorno.


Passaggi specifici per SQL
Query esempio per ogni insight:
Trend di vendita per stagione

sql
Copy code
SELECT 
    Season, 
    SUM(`Purchase Amount (USD)`) AS total_sales
FROM shopping_trends
GROUP BY Season
ORDER BY total_sales DESC;
Clienti top spender

sql
Copy code
SELECT 
    `Customer ID`, 
    SUM(`Purchase Amount (USD)`) AS total_spent
FROM shopping_trends
GROUP BY `Customer ID`
ORDER BY total_spent DESC
LIMIT 10;
Vendite per regione geografica

sql
Copy code
SELECT 
    Location, 
    SUM(`Purchase Amount (USD)`) AS total_sales, 
    COUNT(DISTINCT `Customer ID`) AS unique_customers
FROM shopping_trends
GROUP BY Location
ORDER BY total_sales DESC;
Performance delle categorie di prodotti

sql
Copy code
SELECT 
    Category, 
    AVG(`Review Rating`) AS avg_rating, 
    SUM(`Purchase Amount (USD)`) AS total_sales
FROM shopping_trends
GROUP BY Category
ORDER BY total_sales DESC;
Analisi fidelizzazione

sql
Copy code
SELECT 
    `Customer ID`, 
    COUNT(*) AS total_orders, 
    AVG(`Purchase Amount (USD)`) AS avg_order_value
FROM shopping_trends
WHERE `Previous Purchases` > 0
GROUP BY `Customer ID`
ORDER BY total_orders DESC;

Passaggi specifici per Tableau
Importazione dei dati

Carica il dataset shopping_trends.csv in Tableau.
Verifica i tipi di dati delle colonne (es. numerico, stringa).
Visualizzazioni chiave

Trend stagionale:
Crea un grafico a barre per il fatturato totale per stagione.
Analisi geografica:
Usa una mappa per visualizzare il totale delle vendite per regione (Location).
Top spender:
Usa un grafico a barre per mostrare i primi 10 clienti.
Performance per categoria:
Un grafico a torta o a barre per mostrare il contributo di ciascuna categoria alle vendite totali.

Dashboard interattiva

Combina tutte le visualizzazioni in una dashboard.
Aggiungi filtri interattivi (es. per stagione, regione, categoria).


1. Analisi Avanzata del Comportamento del Cliente
Segmentazione clienti:

Dividi i clienti in segmenti basati su:
Fatturato totale (Purchase Amount (USD)).
Frequenza degli acquisti (Frequency of Purchases).
Preferenza di pagamento (Preferred Payment Method).

Crea cluster di clienti (ad esempio, tramite k-means clustering con scikit-learn) per identificare i profili di spesa.
Cohort Analysis:

Analizza il comportamento di acquisto dei clienti in base alla data del loro primo acquisto o a stagioni specifiche.
2. Performance dei Prodotti
Cross-selling:

Identifica le combinazioni di articoli acquistati insieme.
Esempio: utilizza una analisi di market basket per scoprire associazioni (es. Blusa + Jeans).
Elasticità dei prezzi:

Analizza l’effetto di sconti (Discount Applied) o promozioni (Promo Code Used) sul volume delle vendite.
Analisi delle recensioni:

Studia la correlazione tra Review Rating e le vendite per categoria o prodotto.
3. Analisi Geografica e Temporale
Modello di vendita per area geografica:

Analizza la correlazione tra la posizione (Location) e la spesa media per cliente.
Identifica regioni con potenziale di crescita.
Vendite stagionali per categoria:

Esamina quali categorie dominano durante le diverse stagioni (Season).
4. Analisi della Fedeltà dei Clienti
RFM Analysis:

Classifica i clienti secondo:
Recency (tempo dall'ultimo acquisto).
Frequency (numero di acquisti).
Monetary (spesa totale).
Customer Lifetime Value (CLV):

Calcola il valore futuro stimato dei clienti basato sulle loro abitudini di spesa.
5. Previsioni e Trend
Previsione delle vendite:

Utilizza tecniche di time series analysis (ad esempio con ARIMA o Prophet) per prevedere i trend futuri basati sui dati temporali.
Analisi delle tendenze:

Usa Season + Category per prevedere quali categorie saranno più richieste in un determinato periodo.
Esempi di Query per Insight Avanzati
Identificazione delle combinazioni di articoli più vendute:

sql
Copy code
SELECT 
    `Item Purchased`, 
    COUNT(`Item Purchased`) AS item_count
FROM shopping_trends
GROUP BY `Item Purchased`
ORDER BY item_count DESC;
Elasticità dei prezzi:

sql
Copy code
SELECT 
    `Discount Applied`, 
    AVG(`Purchase Amount (USD)`) AS avg_spent,
    COUNT(`Customer ID`) AS num_customers
FROM shopping_trends
GROUP BY `Discount Applied`;
RFM Analysis:

sql
Copy code
SELECT 
    `Customer ID`, 
    MAX(`Purchase Amount (USD)`) AS recency, 
    COUNT(`Purchase Amount (USD)`) AS frequency, 
    SUM(`Purchase Amount (USD)`) AS monetary
FROM shopping_trends
GROUP BY `Customer ID`;
Dashboard Tableau Approfondita
KPI Avanzati:

Percentuale di clienti ricorrenti vs nuovi clienti.
Incremento delle vendite dopo sconti o promozioni.
Mappa delle Opportunità:

Evidenzia le aree geografiche sottoperformanti in base alla spesa media.
Predizioni Interattive:

Includi un grafico delle previsioni di vendita future.
