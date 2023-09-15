#!/usr/bin/python3
"""
This is a script that lists all cities from the database hbtn_0e_4_usa.
The script uses parameterized queries preventing SQL injection.
"""

import MySQLdb
import sys


def list_cities(user, password, database):
    """
    Access and displays all cities from the database.
    """
    db = MySQLdb.connect(
        host='localhost',
        user=user,
        port=3306,
        passwd=password,
        db=database
    )

    with db.cursor() as cursor:
        myquery = "SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states \
                   ON cities.state_id = states.id \
                   ORDER BY cities.id ASC"

        cursor.execute(myquery)

        cities = cursor.fetchall()

    if cities is not None:
        for city in cities:
            print(city)


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_cities(user, password, database)
