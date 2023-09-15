#!/usr/bin/python3
"""
This is a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(db_url):
    """
    Access and list all State objects that contain letter a.
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    filter_objs = session.query(State).filter(State.name.contains('a'))

    for obj in filter_objs:
        print("{}: {}".format(obj.id, obj.name))


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )

    list_states(db_url)
