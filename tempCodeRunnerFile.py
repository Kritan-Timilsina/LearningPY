import psycopg2
conn = psycopg2.connect(
    dbname="trial",
    user="postgres",
    password="Kritan@9",
    host="localhost",
    port="5432"
)
print("Connected successfully!")
conn.close()