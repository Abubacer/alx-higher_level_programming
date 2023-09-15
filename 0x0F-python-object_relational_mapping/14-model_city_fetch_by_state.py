#!/usr/bin/python3
"""
This is a script that prints all City objects
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_objs(db_url):
    """
    Access and print all City objects.
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    myquery = session.query(City, State).join(State)

    for _city, _state in myquery.all():
        print("{}: ({}) {}".format(_state.name, _city.id, _city.name))

    session.commit()
    session.close()


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )

    print_objs(db_url)
