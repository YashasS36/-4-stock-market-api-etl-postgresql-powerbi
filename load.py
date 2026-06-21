import pandas as pd
import psycopg2

try:

    print("Reading CSV file...")

    df = pd.read_csv("Output/Clean_Stock_Data.csv")

    print("Rows Found:", len(df))

    print("Connecting to PostgreSQL...")

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database=" stock_market_db",
        user="postgres",
        password="Post@123"
    )

    cursor = conn.cursor()

    print("Connected Successfully")

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
            """,
            (
                row["Date"],
                row["Stock_Symbol"],
                float(row["Open"]),
                float(row["High"]),
                float(row["Low"]),
                float(row["Close"]),
                int(row["Volume"])
            )
        )

    conn.commit()

    print("Data Loaded Successfully")

    cursor.close()
    conn.close()

except Exception as e:

    print("ERROR OCCURRED:")
    print(e)