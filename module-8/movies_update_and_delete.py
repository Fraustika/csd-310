import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'movies_user',
    'password': 'popcorn',
    'host': 'localhost',
    'port': '3306',
    'database': 'movies',
    'raise_on_warnings': True
}

def show_films(cursor, title):
    cursor.execute("""
        SELECT film.film_name AS Name,
               film.film_director AS Director,
               genre.genre_name AS Genre,
               studio.studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    # Display films before any operations
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film
    cursor.execute("""
        INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        VALUES ('Inception', '2010', 148, 'Christopher Nolan', 1, 1)
    """)
    db.commit()

    # Display films after the insert operation
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update the film Alien to Horror
    cursor.execute("""
         UPDATE film
         SET genre_id = 1
         WHERE film_name = 'Alien'
     """)
    db.commit()

    # Display films after the update operation
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    # Delete the film Gladiator
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """)
    db.commit()

    # Display films after the delete operation
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    cursor.close()
    db.close()