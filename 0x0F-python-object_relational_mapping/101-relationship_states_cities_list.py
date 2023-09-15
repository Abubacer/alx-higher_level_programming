#!/usr/bin/python3
"""
This is a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_state_cities(db_url):
    """
    Lists all State objects, and corresponding City objects.
    Format: <state id>: <state name>
            <tabulation><city id>: <city name>
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    myquey = session.query(State).order_by(State.id).all()

    for state in myquey:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("	{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
    list_state_cities(db_url)
