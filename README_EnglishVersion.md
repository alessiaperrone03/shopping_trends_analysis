# **Project 1: E-commerce Database Analysis (SQL + Tableau)**

## **Project Description**
This project aims to explore an e-commerce database to derive strategic insights about customer behaviors, sales, and product performance. Using SQL for data analysis and Tableau to create an interactive dashboard, I will present the findings in a clear and accessible manner.

## **Key Objectives**
1. **Understand Sales Trends:**
   - Analyze monthly/annual revenue.
   - Identify seasonal patterns (e.g., spikes during sales or holidays).

2. **Identify Most Valuable Customers:**
   - Determine the top 10 customers by total revenue.
   - Calculate the average Customer Lifetime Value (CLV).

3. **Evaluate Product Performance:**
   - Identify the best-selling products and those with the highest revenue.

4. **Geographical Behavior Analysis:**
   - Identify the most profitable regions/cities.
   - Calculate the average order value per geographical area.

5. **Study Product Categories:**
   - Analyze which categories generate the most sales.
   - Assess profit margins by category.

6. **Measure Customer Loyalty:**
   - Determine the return rate of customers.
   - Compare unique orders with recurring ones.

## **Dataset**
The dataset used contains several tables, including:
- **orders**: Order details (date, customer ID, product ID).
- **customers**: Customer information (name, address, geographic area).
- **products**: Product details (name, category, price).
- **order_details**: Quantity and prices for each product in an order.

### **Initial Goal**
- Analyze the database structure and map the relationships between tables (ER schema).

## **Advanced Analysis**
1. **Customer Segmentation**
   - Segment customers based on:
     - Total revenue.
     - Purchase frequency.
     - Preferred payment method.
   - Use clustering algorithms like k-means to identify distinct spending profiles.

2. **Cohort Analysis**
   - Analyze purchasing behaviors based on first purchase or specific seasons.

3. **Cross-selling**
   - Identify combinations of items purchased together (e.g., via market basket analysis).

4. **Price Elasticity**
   - Study the impact of discounts and promotions on sales volume.

## **Tableau Visualizations**
### **Main Dashboards**
1. **Overview:**
   - KPIs: Total revenue, total orders, number of customers.
   - Line charts for trend analysis over time.

2. **Customer & Behavior Insights:**
   - Recurring vs. new customers.
   - Visualization of customer segments.

3. **Geographical Analysis:**
   - Interactive map with revenue by region/city.

4. **Product Performance:**
   - Best-selling products and most profitable categories.

5. **Forecasting:**
   - Predictive charts based on time series analysis.

## **Predictive Models and Statistical Analysis**
1. **Sales Forecasting:**
   - Use time series analysis (e.g., ARIMA, Prophet).

2. **Price Elasticity:**
   - Correlation analysis between discounts and sales volume.

3. **Lifetime Value Prediction:**
   - Estimating future customer value to improve marketing strategies.

## **Possible Extensions of the Project**
- Integrate sentiment analysis of reviews to evaluate customer perception of products.
- Implement a model to suggest optimal pricing strategies.
- Connect data to marketing platforms to propose targeted campaigns.

## **Tools Used**
- **SQL**: For data extraction and analysis.
- **Python**:
  - Advanced statistical analysis (pandas, numpy, scikit-learn).
  - Forecasting and clustering.
- **Tableau**: To create interactive dashboards.
- **Jupyter Notebook**: For documenting the workflow.
