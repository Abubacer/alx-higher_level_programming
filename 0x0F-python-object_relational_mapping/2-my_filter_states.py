#!/usr/bin/python3
"""
This is a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def list_states(user, password, database, state):
    """
    Access and displays all values in the states table
    from the database.
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
                    WHERE name LIKE BINARY '{}' \
                    ORDER BY states.id ASC".format(state))

    states = cursor.fetchall()

    for state in states:
        print(state)


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    list_states(user, password, database, state)
