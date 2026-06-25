import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. LOAD CSV USING PANDAS
# ==========================================
# Make sure you have created 'sales_data.csv' in your internspark folder!
try:
    df = pd.read_csv('sales_data.csv')
    print("✅ Step 1: Dataset Loaded Successfully!")
    print("\n--- Initial Raw Data ---")
    print(df)
except FileNotFoundError:
    print("❌ Error: 'sales_data.csv' not found in this folder.")
    print("Please make sure you created the CSV file before running this script.")
    exit()

# ==========================================
# 2. PERFORM DATA CLEANING
# ==========================================
print("\n--- Step 2: Data Cleaning ---")
print("Missing values per column before cleaning:")
print(df.isnull().sum())

# Drop rows with missing values and remove duplicate rows
df_cleaned = df.dropna().drop_duplicates().copy()

# Add a calculated column (Total Revenue) to add value to the data
df_cleaned['Revenue'] = df_cleaned['Price'] * df_cleaned['Quantity']
print("\n--- Cleaned Data with Revenue Column ---")
print(df_cleaned)

# ==========================================
# 3. FILTERING & GROUPING
# ==========================================
print("\n--- Step 3: Filtering & Grouping ---")

# Filtering: Find rows where the total Revenue is greater than $100
high_revenue_df = df_cleaned[df_cleaned['Revenue'] > 100]
print("Filtered Data (Revenue > 100):\n", high_revenue_df)

# Grouping: Sum up total revenue per Product Category
grouped_df = df_cleaned.groupby('Category')['Revenue'].sum().reset_index()
print("\nTotal Revenue Grouped by Category:\n", grouped_df)

# ==========================================
# 4. GENERATE INSIGHTS (Summary Statistics)
# ==========================================
print("\n--- Step 4: Summary Insights ---")
print(df_cleaned.describe())

# ==========================================
# 5. GENERATE & SAVE GRAPHS (Optional Deliverable)
# ==========================================
try:
    plt.figure(figsize=(6, 4))
    sns.barplot(x='Category', y='Revenue', data=grouped_df, palette='Set2')
    plt.title('Total Revenue by Category')
    plt.tight_layout()

    # Automatically saves the chart inside your internspark folder
    plt.savefig('task3_chart.png')
    print("\n📊 Chart successfully generated and saved as 'task3_chart.png'!")
    plt.show()
except Exception as e:
    print(f"\nCould not generate graph: {e}")