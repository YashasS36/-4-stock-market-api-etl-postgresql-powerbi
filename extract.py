import pandas as pd
import yfinance as yf

stocks = ["AAPL", "MSFT", "TSLA", "INFY", "TCS.NS"]

all_data = []

for stock in stocks:

    df = yf.download(stock, period="1mo")

    # Remove MultiIndex
    df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    df["Stock_Symbol"] = stock

    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

print(final_df.columns)

final_df.to_csv(
    "Output/Raw_Stock_Data.csv",
    index=False
)

print("Data Extracted Successfully")