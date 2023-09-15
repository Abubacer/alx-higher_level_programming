#!/usr/bin/python3
"""
This is a script that lists all State objects
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(db_url):
    """
    Access and list all State objects.
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    for obj in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(obj.id, obj.name))


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )

    list_states(db_url)
