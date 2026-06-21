import pandas as pd
import psycopg2

df = pd.read_csv("Output/Clean_Stock_Data.csv")

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database=" stock_market_db",
    user="postgres",
    password="Post@123"
)

cursor = conn.cursor()

rows_loaded = 0

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO stock_prices
        (
            trade_date,
            stock_symbol,
            open_price,
            high_price,
            low_price,
            close_price,
            volume
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (trade_date, stock_symbol)
        DO NOTHING;
        """,
        (
            row["Date"],
            row["Stock_Symbol"],
            row["Open"],
            row["High"],
            row["Low"],
            row["Close"],
            row["Volume"]
        )
    )

    rows_loaded += cursor.rowcount

conn.commit()

print(f"New Rows Loaded: {rows_loaded}")

cursor.close()
conn.close()