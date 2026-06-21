import pandas as pd

df = pd.read_csv("Output/Raw_Stock_Data.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Convert date format
df["Date"] = pd.to_datetime(df["Date"])

# Round prices
for col in ["Open", "High", "Low", "Close"]:
    df[col] = df[col].round(2)

# Sort records
df = df.sort_values(
    by=["Stock_Symbol", "Date"]
)

df.to_csv(
    "Output/Clean_Stock_Data.csv",
    index=False
)

print("Transformation Completed")
print(df.head())