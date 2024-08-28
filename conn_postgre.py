import psycopg2

conn = psycopg2.connect(database="chenil_v4",
                        host = "52.17.83.182",
                        user = "daniel",
                        password= "datascientest",
                        port = "5432")

cur = conn.cursor()

cur.execute("SELECT * FROM Chiens LIMIT 10;")

rows = cur.fetchall()
for row in rows:
    print(row)
    
cur.close()

conn.close()