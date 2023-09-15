#!/usr/bin/python3
"""
This is a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_obj(db_url):
    """
    Adds and prints the State object.
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
    session.close()


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
    insert_obj(db_url)
