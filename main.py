import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '123456'
database = 'lab3'
host = 'localhost'
port = '5433'

query_create = '''
CREATE VIEW countbygenre AS 
SELECT genre_type, COUNT(name) AS film_count
FROM title_genre
GROUP BY genre_type;

CREATE VIEW countbytype AS 
SELECT title_type, COUNT(name) AS film_count
FROM Title
GROUP BY title_type;

CREATE VIEW countbyyear AS 
SELECT release_year, COUNT(name) AS film_count
FROM Title
GROUP BY release_year
ORDER BY release_year;
'''

query_1 = '''
SELECT * FROM countbygenre;
'''

query_2 = '''
SELECT * FROM countbytype;
'''

query_3 = '''
SELECT * FROM countbyyear;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))
with conn:
                       
    print ("Database opened successfully")
    cur = conn.cursor()

    cur.execute(query_1)
    result_1 = cur.fetchall()
    print('Результати запиту 1:')
    for row in result_1:
        print(row)


    genres = [row[0] for row in result_1]
    film_counts = [row[1] for row in result_1]

    plt.bar(genres, film_counts, color='blue')
    plt.title('Кількість фільмів кожного жанру')
    plt.xlabel('Жанр')
    plt.ylabel('Кількість фільмів')
    plt.show()

    cur.execute(query_2)
    result_2 = cur.fetchall()
    print('\nРезультати запиту 2:')
    for row in result_2:
        print(row)

    title_types = [row[0] for row in result_2]
    film_counts_by_title_type = [row[1] for row in result_2]

    plt.pie(film_counts_by_title_type, labels=title_types, autopct='%1.1f%%', startangle=90)
    plt.title('Кількість фільмів за типом')
    plt.axis('equal') 
    plt.show()

    cur.execute(query_3)
    result_3 = cur.fetchall()
    print('\nРезультати запиту 3:')
    for row in result_3:
        print(row)

    years = [row[0] for row in result_3]
    film_counts_by_year = [row[1] for row in result_3]

    plt.plot(years, film_counts_by_year, marker='o', linestyle='-', color='green')
    plt.title('Залежність фільмів від року')
    plt.xlabel('Рік')
    plt.ylabel('Кількість фільмів')
    plt.grid(True)
    plt.show()
