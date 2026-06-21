import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="Post@123"
    )

    print("Connected Successfully\n")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT datname
        FROM pg_database
        ORDER BY datname;
    """)

    databases = cursor.fetchall()

    print("Available Databases:")
    for db in databases:
        print(repr(db[0]))

    cursor.close()
    conn.close()

except Exception as e:
    print("ERROR:")
    print(e)