import csv
import psycopg2

username = 'postgres'
password = '123456'
database = 'lab3.2'
host = 'localhost'
port = '5433'

INPUT_CSV_FILE = 'imdb_movies_shows.csv'

query_title00 = '''
DROP TABLE IF EXISTS title_new CASCADE
'''
query_genre00 = '''
DROP TABLE IF EXISTS genre_new CASCADE
'''
query_title_genre00 = '''
DROP TABLE IF EXISTS title_genre_new CASCADE
'''

query_title0 = '''
CREATE TABLE title_new
(
  name VARCHAR(100) NOT NULL, 
  title_type VARCHAR(50) NOT NULL, 
  release_year VARCHAR(50) NOT NULL,
  PRIMARY KEY (name)
)
'''
query_title_genre0= '''
CREATE TABLE title_genre_new
(
  name VARCHAR(100) NOT NULL, 
  genre_type VARCHAR(50) NOT NULL, 
  FOREIGN KEY (name) REFERENCES Title(name),
  FOREIGN KEY (genre_type) REFERENCES Genre(genre_type)
)
'''
query_genre0 = '''
CREATE TABLE genre_new
(
  genre_type VARCHAR(50) NOT NULL, 
  PRIMARY KEY (genre_type)
);
'''

query_title1 = '''
DELETE FROM title_new
'''
query_title_genre1 = '''
DELETE FROM title_genre_new
'''
query_genre1 = '''
DELETE FROM genre_new
'''

query_title2 = '''
INSERT INTO title_new (name, title_type, release_year) VALUES (%s, %s, %s)
'''
query_title_genre2 = '''
INSERT INTO title_genre_new (name, genre_type) VALUES (%s, %s)
'''
query_genre2 = '''
INSERT INTO genre_new (genre_type) VALUES (%s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_title00)
    cur.execute(query_title0)
    cur.execute(query_genre00)
    cur.execute(query_genre0)
    cur.execute(query_title_genre00)
    cur.execute(query_title_genre0)
    
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        genres = []
        for idx, row in enumerate(reader):
            print(idx)
            title_values = (row['Name'], row['Title type'], row['Release year'])
            cur.execute(query_title2, title_values)
            for genre in row['Genre'].split(', '):        
                if genre not in genres:
                    cur.execute(query_genre2, [genre])
                    genres.append(genre)
                title_genre_values = (row['Name'], genre)
                cur.execute(query_title_genre2, title_genre_values)
            

    conn.commit()
