import pandas as pd

df = pd.read_csv("Output/Raw_Stock_Data.csv")

print("\n===== DATA VALIDATION REPORT =====\n")

print("Total Rows:")
print(len(df))

print("\nTotal Columns:")
print(len(df.columns))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nColumn Names:")
print(df.columns.tolist())