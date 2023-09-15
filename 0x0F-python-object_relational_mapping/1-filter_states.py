#!/usr/bin/python3
"""
This is a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(user, password, database):
    """
    Access and list the states from the database.
    """
    db = MySQLdb.connect(
        host='localhost',
        user=user,
        port=3306,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(user, password, database)
