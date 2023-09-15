#!/usr/bin/python3
"""
This is a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_obj(db_url):
    """
    Deletes all State objects with a name containing the letter a.
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    filter_obj = session.query(State).filter(State.name.contains('a'))
    for obj in filter_obj:
        session.delete(obj)

    session.commit()
    session.close()


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
    delete_obj(db_url)
