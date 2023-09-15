#!/usr/bin/python3
"""
This is a script  takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.

The script uses parameterized queries preventing SQL injection.
"""

import MySQLdb
import sys


def list_cities(user, password, database, state):
    """
    Access and displays all cities of a state from the database.
    """
    db = MySQLdb.connect(
        host='localhost',
        user=user,
        port=3306,
        passwd=password,
        db=database
    )

    with db.cursor() as cursor:
        myquery = "SELECT cities.id, cities.name \
                   FROM cities JOIN states \
                   ON cities.state_id = states.id \
                   WHERE states.name LIKE %s \
                   ORDER BY cities.id ASC"

        cursor.execute(myquery, (state,))

        cities = cursor.fetchall()

    if cities is not None:
        print(", ".join([city[1] for city in cities]))


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    list_cities(user, password, database, state)
