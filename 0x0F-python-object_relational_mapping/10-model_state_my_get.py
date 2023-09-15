#!/usr/bin/python3
"""
This is a script that that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_obj(db_url, state):
    """
    Access and print the State object.
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    filter_obj = session.query(State).filter(State.name == state).first()

    if filter_obj:
        print("{}".format(filter_obj.id))
    else:
        print("Not found")


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
    state = sys.argv[4]
    print_obj(db_url, state)
