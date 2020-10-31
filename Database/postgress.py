#%%
import psycopg2 as pg

#%%
conn = pg.connect(host="localhost", port = 5432, database="helloworld", user="postgres", password="root")

cur = conn.cursor()

cur.execute("""SELECT * FROM world""")
query_results = cur.fetchall()
print(query_results)

cur.close()
conn.close()


#//TODO Insert
#//TODO Update, Delete
