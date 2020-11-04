#%%
import psycopg2 as pg

#%%


cur = conn.cursor()

cur.execute("""SELECT * FROM world""")
query_results = cur.fetchall()
print(query_results)

cur.close()
conn.close()

#%%
from configparser import ConfigParser

def config(filename='database,ini', section='postgresql'):
    parser =ConfigParser()
    parser.read(filename)

    db = {}
    
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1}'.format(section, filename))

        return db
#//TODO Insert
#//TODO Update, Delete

# %%
