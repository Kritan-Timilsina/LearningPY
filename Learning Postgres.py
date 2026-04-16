import psycopg2

conn = psycopg2.connect(
    dbname="Trial",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5433"
)

cur = conn.cursor()
cur.execute("SELECT * FROM Students;")
rows = cur.fetchall()

for row in rows:
    print(row)
conn.close()