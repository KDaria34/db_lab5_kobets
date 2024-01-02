import json
import psycopg2

username = 'postgres'
password = '123456'
database = 'lab3.2'
host = 'localhost'
port = '5433'


conn = psycopg2.connect(user=username, password=password, dbname=database)

data = {}
with conn:

    cur = conn.cursor()
    
    for table in ('title_new', 'title_genre_new',  'genre_new',):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('all_data.json', 'w') as outf:
    json.dump(data, outf, default = str)
