Section 1: Data Understanding & Cleaning (Pandas + NumPy)
PS1. Dataset Overview
Load the dataset
Display shape, column names, and data types
Identify numerical vs categorical columns

PS2. Missing Value Analysis
Identify columns with missing values
Calculate percentage of missing values per column
Decide which columns need cleaning

PS3. Cleaning Boolean Column
Clean the Discount Applied column
Convert missing values to a meaningful category (e.g., False or Unknown)
Verify unique values after cleaning

PS4. Date Conversion & Feature Extraction
Convert Transaction Date to datetime
Extract:
Year
Month
Day
Section 2: Sales & Revenue Analysis (Pandas)
PS5. Category-wise Sales Performance
Calculate total revenue (Total Spent) per Category
Sort results in descending order

PS6. Item-level Analysis
Identify top 10 items based on:
Total quantity sold
Total revenue

PS7. Customer Spending Behavior
Calculate total spending per Customer ID
Identify top 5 highest-spending customers

PS8. Payment Method Analysis
Calculate:
Total transactions per Payment Method
Total revenue per Payment Method

Section 3: NumPy-based Insights
PS9. Price Statistics Using NumPy
Using NumPy, calculate:
Mean
Median
Standard deviation
of Price Per Unit

PS10. High-Value Transactions
Using NumPy conditions, identify transactions where:
Total Spent is greater than the 90th percentile

Section 4: Time-Based Analysis (Pandas)
PS11. Monthly Revenue Trend
Calculate monthly total revenue
Identify the best-performing month

PS12. Year-wise Sales Growth
Analyze year-wise total revenue
Calculate year-over-year growth percentage

Section 5: Matplotlib Visualizations
PS13. Revenue by Category (Bar Chart)
Plot total revenue per category
Sort categories by revenue
Add labels, title, and grid

PS14. Monthly Sales Trend (Line Chart)
Plot monthly revenue trend
Highlight peak month

PS15. Distribution of Transaction Amounts (Histogram)
Plot histogram of Total Spent
Analyze skewness and outliers

Section 6: Seaborn Visual Analytics
PS16. Category vs Revenue (Seaborn Bar Plot)
Plot average Total Spent per Category
Use confidence intervals

PS17. Price vs Quantity (Scatter Plot)
Plot Price Per Unit vs Quantity
Use Category as hue
Interpret buying behavior

PS18. Payment Method Distribution (Count Plot)
Visualize number of transactions per payment method
Compare online vs offline preference

PS19. Discount Impact Analysis
Compare average Total Spent for:
Discount Applied = True
Discount Applied = False
Visualize using Seaborn

PS20. Correlation Heatmap
Compute correlation matrix for numerical columns
Visualize using a Seaborn heatmap
Interpret strongest relationships