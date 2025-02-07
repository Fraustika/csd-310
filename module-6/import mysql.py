import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values

secrets = dotenv_values(".env")
config = {
    "user": secrets["movies_user"],
    "password": secrets["popcorn"],
    "host": secrets["localhost"],
    "database": secrets["movies"],
    "raise_on_warnings": True #not in .env file
}

try:
    db = mysql.connector.connect(**config)  # connect to the movies database

    # output the connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                       config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:


    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()



