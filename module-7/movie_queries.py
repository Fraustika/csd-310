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

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    # First query: Select all fields from the studio table
    cursor.execute("SELECT * FROM studio")
    studio_records = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for record in studio_records:
        print(f"Studio ID: {record[0]} \nStudio Name: {record[1]}")
        print("")  # Add a space between records

    # Second query: Select all fields from the genre table
    cursor.execute("SELECT * FROM genre")
    genre_records = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for record in genre_records:
        print(f"Genre ID: {record[0]} \nGenre Name: {record[1]}")
        print("")  # Add a space between records

    # Third query: Select names and runtimes of movies with a runtime of less than two hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_movies = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for movie in short_movies:
        print(f"Film Name: {movie[0]} \nFilm Runtime: {movie[1]} minutes")
        print("")  # Add a space between records

    # Fourth query: Get a list of movie names and directors grouped by director and display film first
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films_directors = cursor.fetchall()
    print("-- DISPLAYING Film and Director RECORDS in ORDER --")
    for record in films_directors:
        print(f"Film: {record[0]} \nDirector: {record[1]}")
        print("")  # Add a space between records

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