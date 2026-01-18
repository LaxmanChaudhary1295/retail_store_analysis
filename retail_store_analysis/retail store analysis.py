import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns



##PS1
retail_store = pd.read_csv("D:\\Data Science\\Python Programing\\Python Library - Seaborn\\retail_store_analysis\\dataset\\retail_store_sales.csv")
print(retail_store)
print(retail_store.shape)
print(retail_store.columns)
print(retail_store.dtypes)

##PS2
missing_values = retail_store.isnull().sum()
print(missing_values)
total_rows = retail_store.shape[0]
missing_values_percentage = (retail_store.isnull().sum() / total_rows)*100
print(missing_values_percentage)
which_columns_need_cleaning = missing_values_percentage[missing_values_percentage>0].sort_values(ascending=False)
print("Colunms Names:\n",which_columns_need_cleaning)

#PS3
clean_DAC =retail_store.fillna(
    {"Discount Applied":"Unknown"}
)
print(clean_DAC)

#PS4
retail_store["Transaction Date"] = pd.to_datetime(retail_store["Transaction Date"],dayfirst=True, errors='coerce')
retail_store["Day"]= retail_store["Transaction Date"].dt.day
retail_store["Month"]= retail_store["Transaction Date"].dt.month
retail_store["Year"]= retail_store["Transaction Date"].dt.year
print(retail_store[["Day","Month","Year"]].head(10))

# #PS5
total_revenue = (retail_store
                 .groupby("Category",as_index=False)["Total Spent"]
                 .sum()
                 .sort_values("Total Spent",ascending=False))
print(total_revenue)

total_revenue.plot(kind = 'bar', x="Category", y="Total Spent", color = "cornsilk",edgecolor ="black", label=" Category-wise Sales Performance")
plt.xlabel("Category")
plt.ylabel("Total Spent")
plt.ylim(170000,210000 )
plt.grid(linestyle =":", linewidth =0.5, color ="hotpink")
plt.legend()
plt.title("Category-wise Sales Performance")
plt.tight_layout()
plt.savefig("Category-wise Sales Performance",dpi = 250, bbox_inches ="tight")
plt.show()

#PS6
item_level =(
    retail_store
    .groupby("Item", as_index=False)
             .agg(
                 Total_Quantity=("Quantity","sum"),
                 Total_Revenue =("Total Spent","sum")
             )
)
top_10_items =(item_level
               .sort_values(by="Total_Quantity",ascending=False)
               .head(10))
print(top_10_items)

top_10_items.plot(kind="bar", x ="Item", y ="Total_Quantity", color="tomato",edgecolor ="black", label="Top 10 Items")
plt.xlabel("Item")
plt.ylabel("Quantity")
plt.grid(linestyle =":", linewidth =0.5, color ="hotpink")
plt.legend()
plt.title("Identify top 10 items")
plt.tight_layout()
plt.savefig("Identify top 10 items",dpi = 250, bbox_inches ="tight")
plt.show()

#PS7

total_spent_per_ci = (
    retail_store
    .groupby("Customer ID",as_index=False)
    .agg(
        Total_Spent =("Total Spent", "sum")

    )
)

top_5_highest_spending_customers =(total_spent_per_ci
                                   .sort_values("Total_Spent",
                                   ascending=False)
                                   .head(5))
print(top_5_highest_spending_customers)
top_5_highest_spending_customers.plot(kind="pie", y="Total_Spent",
                                      labels =top_5_highest_spending_customers["Customer ID"],
                                      color=["teal","cyan","purple","hotpink","peru"],
                                      wedgeprops={'edgecolor': 'black', 'linewidth':1.5}, 
                                      autopct ="%.1f%%", 
                                      startangle =90,
                                      legend = False)
plt.title("Highest Spending Customers")
plt.title("Top 5 highest-spending customers")
plt.tight_layout()
plt.savefig("Top 5 highest-spending customers",dpi = 250, bbox_inches ="tight")
plt.show()


#PS8
payment_method =(
    retail_store
    .groupby("Payment Method", as_index=False)
    .agg(
        Total_transaction =("Payment Method","count"),
        Total_revenue =("Total Spent","sum")
    )
)
print(payment_method)

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 6), sharex=True)


ax[0].plot(
    payment_method["Payment Method"],
    payment_method["Total_transaction"],
    linestyle="-",
    linewidth=1,
    marker=">",
    color="slateblue",
    label="Total Transactions"
)
ax[0].set_title("Total Transactions by Payment Method", fontsize=9)
ax[0].set_ylabel("Transactions")
ax[0].legend()
ax[0].grid(True)


ax[1].plot(
    payment_method["Payment Method"],
    payment_method["Total_revenue"],
    linestyle="-",
    linewidth=1.5,
    marker="o",
    color="peru",
    label="Total Revenue"
)
ax[1].set_title("Total Revenue by Payment Method", fontsize=9)
ax[1].set_xlabel("Payment Method")
ax[1].set_ylabel("Revenue")
ax[1].legend()
ax[1].grid(True)

plt.suptitle("Payment method analysis")
plt.tight_layout()
plt.savefig("Payment method analysis",dpi = 250, bbox_inches ="tight")
plt.show()




#PS9

price_mean = np.nanmean(retail_store["Price Per Unit"])
price_median = np.nanmedian(retail_store["Price Per Unit"])
price_std = np.nanstd(retail_store["Price Per Unit"])
print("Mean:",price_mean)
print("Median:",price_median) 
print("Standard Deviation:",price_std)

#PS10
p90 = np.nanpercentile(retail_store["Total Spent"], 90)
print("90th Percentile of Total Spent:", p90)

high_value_transactions = retail_store[
    retail_store["Total Spent"].to_numpy() > p90
]

print(high_value_transactions)
print("High-value transaction count:", len(high_value_transactions))

#PS11
retail_store["Transaction Date"] = pd.to_datetime(retail_store["Transaction Date"], errors='coerce')
retail_store["Month"] = retail_store["Transaction Date"].dt.month
monthly_total_revenue = (retail_store
                         .groupby("Month", as_index=False)
                         .agg(
                             Total_revenue =("Total Spent","sum")
                         ))
print(monthly_total_revenue)

best_month = monthly_total_revenue.loc[
    monthly_total_revenue["Total_revenue"].idxmax()
]

print("Best Performing Month:")
print(best_month)

plt.plot(monthly_total_revenue["Month"], 
         monthly_total_revenue["Total_revenue"],
         linestyle ="-",
         linewidth = 1, 
         color ="mediumturquoise", 
         marker ="o", 
         label = "Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
plt.xlim(1,12)
plt.ylim(40000,60000)
plt.legend()
plt.title("Montly revenue trend")
plt.tight_layout()
plt.savefig("Montly revenue trend",dpi = 250, bbox_inches ="tight")
plt.show()

#PS12
retail_store["Transaction Date"] =pd.to_datetime(retail_store["Transaction Date"],dayfirst=True,errors="coerce")
retail_store["Year"] = retail_store["Transaction Date"].dt.year

year_wise_total_revenue = (
    retail_store
    .groupby("Year", as_index=False)
    .agg(
        Total_revenue = ("Total Spent","sum")
    )
)
print(year_wise_total_revenue)

year_wise_total_revenue["YoY_Growth_%"] = (
    year_wise_total_revenue["Total_revenue"]
    .pct_change() * 100
)

print(year_wise_total_revenue)

plt.plot(year_wise_total_revenue["Year"], 
         year_wise_total_revenue["Total_revenue"],
         linestyle ="-",
         linewidth = 1, 
         color ="mediumorchid", 
         marker ="<", 
         label = "Yearly Revenue")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.xticks([2022.0,2023.0,2024.0,2025.0],[2022,2023,2024,2025])
plt.legend()
plt.title("Year-wise Sales Growth")
plt.tight_layout()
plt.savefig("Year-wise Sales Growth",dpi = 250, bbox_inches ="tight")
plt.show()

#PS13

total_revenue = (retail_store
                 .groupby("Category",as_index=False)["Total Spent"]
                 .sum()
                 .sort_values("Total Spent",ascending=False))
print(total_revenue)

total_revenue.plot(kind = 'bar', x="Category", y="Total Spent", color = "cornsilk",edgecolor ="black", label=" Category-wise Sales Performance")
plt.xlabel("Category")
plt.ylabel("Total Spent")
plt.ylim(170000,210000 )
plt.grid(linestyle =":", linewidth =0.5, color ="hotpink")
plt.legend()
plt.title("Revenue by Category")
plt.tight_layout()
plt.savefig("Revenue by Category",dpi = 250, bbox_inches ="tight")
plt.show()

#PS14

retail_store["Transaction Date"] = pd.to_datetime(
    retail_store["Transaction Date"], dayfirst=True, errors="coerce"
)

retail_store["Month"] = retail_store["Transaction Date"].dt.month

monthly_total_revenue = (
    retail_store
    .groupby("Month", as_index=False)
    .agg(Total_revenue=("Total Spent", "sum"))
)


peak_row = monthly_total_revenue.loc[
    monthly_total_revenue["Total_revenue"].idxmax()
]

peak_month = peak_row["Month"]
peak_revenue = peak_row["Total_revenue"]


plt.figure(figsize=(9, 5))
plt.plot(
    monthly_total_revenue["Month"],
    monthly_total_revenue["Total_revenue"],
    linestyle="-",
    linewidth=1,
    color="mediumturquoise",
    marker="o",
    label="Monthly Revenue"
)


plt.scatter(
    peak_month,
    peak_revenue,
    color="crimson",
    s=120,
    zorder=5,
    label="Peak Month"
)


plt.annotate(
    f"Peak: {int(peak_revenue)}",
    (peak_month, peak_revenue),
    textcoords="offset points",
    xytext=(0, 8),
    ha="center",
    fontsize=9
)

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(
    range(1, 13),
    ["Jan","Feb","Mar","Apr","May","Jun",
     "Jul","Aug","Sep","Oct","Nov","Dec"]
)

plt.ylim(
    monthly_total_revenue["Total_revenue"].min() * 0.95,
    monthly_total_revenue["Total_revenue"].max() * 1.05
)

plt.legend()
plt.grid(linestyle=":", linewidth=0.5)
plt.tight_layout()
plt.title("Monthly Sales Trend")
plt.savefig("Monthly Sales Trend",dpi = 250, bbox_inches ="tight")
plt.show()


##PS15

total_spent = retail_store["Total Spent"].dropna()
print(total_spent)

plt.hist(total_spent, color="plum", bins =8,edgecolor ="black")
plt.xlabel("Total Spent per Transaction")
plt.ylabel("Frequency")
plt.title("Distribution of Transaction Amounts")
plt.grid(axis="y", linestyle=":", linewidth=0.5)
plt.title("Distribution of Transaction Amounts")
plt.tight_layout()
plt.savefig("Distribution of Transaction Amounts",dpi = 250, bbox_inches ="tight")
plt.show()

#PS16

total_revenue = (retail_store
                 .groupby("Category",as_index=False)["Total Spent"]
                 .mean()
                 .sort_values("Total Spent",ascending=False))
print(total_revenue)

sns.barplot(data=total_revenue,
            x="Category", 
            y="Total Spent",
            ci=None, 
            estimator="mean",
            color="cyan",
            edgecolor="black")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.title("Average Total Spent per Category")
plt.grid(axis="y", linestyle=":", linewidth=0.5)
plt.xticks(rotation=90)
plt.title("Average Total Spent per Category")
plt.tight_layout()
plt.savefig("Average Total Spent per Category",dpi = 250, bbox_inches ="tight")
plt.show()

#PS17
Price_vs_Quantity =pd.DataFrame(retail_store["Price Per Unit"],
                                retail_store["Quantity"],
                                retail_store["Category"])
sns.scatterplot(
    data=retail_store,
    x="Price Per Unit",
    y="Quantity",
    hue="Category",
    alpha=0.7
)

plt.xlabel("Price Per Unit")
plt.ylabel("Quantity Purchased")
plt.title("Price vs Quantity by Category")
plt.grid(linestyle=":", linewidth=0.5)
plt.title("Price Per Unit vs Quantity")
plt.tight_layout()
plt.savefig("Price Per Unit vs Quantity",dpi = 250, bbox_inches ="tight")
plt.show()


#PS18

transaction =(
    retail_store
    .groupby("Payment Method", as_index=False)
    .agg(
        Total_transaction =("Payment Method","count")
    )
)
print(transaction)

sns.countplot(
    data=retail_store,
    x="Payment Method",
    color="rosybrown"
)

plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.title("Transaction Count by Payment Method")
plt.grid(axis="y", linestyle=":", linewidth=0.5)
plt.title("Online vs offline preference")
plt.tight_layout()
plt.savefig("Online vs offline preference",dpi = 250, bbox_inches ="tight")
plt.show()


#PS19

average_total_spent_by_discount =(
    retail_store.
    groupby(
        "Discount Applied", as_index=False
    ).agg(
        avg_total_spent =("Total Spent","mean")
    )
)
print(average_total_spent_by_discount)

sns.barplot(data=average_total_spent_by_discount, 
             x=average_total_spent_by_discount["Discount Applied"],
             y="avg_total_spent",
             color="fuchsia")
plt.xlabel("Discount Applied")
plt.ylabel("Average Total Spent")
plt.title("Impact of Discount on Spending")
plt.grid(axis="y", linestyle=":", linewidth=0.5)
plt.title("Discount Impact Analysis")
plt.tight_layout()
plt.savefig("Discount Impact Analysis",dpi = 250, bbox_inches ="tight")
plt.show()

#PS20

numerical_df =retail_store.select_dtypes(include=[np.number])
corr_matrix = numerical_df.corr(method="spearman")
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    linecolor="white"
)

plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.savefig("Correlation Heatmap of Numerical Features",dpi = 250, bbox_inches ="tight")
plt.show()