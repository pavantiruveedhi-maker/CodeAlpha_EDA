import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load data and clean empty artifact structural lines
df = pd.read_csv("D:\\Code_Alpha_projects\\Unemployment in India.csv", skipinitialspace=True)
df = df.dropna(how='all').reset_index(drop=True)

# Clean structural white space gaps from column headers
df.columns = df.columns.str.strip()

# 2. Type Corrections
df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y', errors='coerce')
df['Region'] = df['Region'].astype(str).str.strip()
df['Area'] = df['Area'].astype(str).str.strip()

# 3. Structural Assessment Breakdown
print("--- Dataset Shape Check ---")
print(f"Total Active Rows: {df.shape[0]} | Clean Explored Columns: {df.shape[1]}\n")

print("--- Missing Entries Mapping Summary ---")
print(df.isna().sum())

# 4. Generate Core Statistical Aggregates
print("\n--- Numerical Distributions Overview ---")
print(df.describe().T)

# 5. Visual Correlation Matrix Heatmap Analysis
plt.figure(figsize=(8, 5))
numeric_cols = ['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Macroeconomic Metrics Matrix Correlation Heatmap')
plt.show()
