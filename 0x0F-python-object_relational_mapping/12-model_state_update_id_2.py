#!/usr/bin/python3
"""
This is a script that changes the name of a State object
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_obj(db_url):
    """
    Changes and prints the State object.
    """
    db_engine = create_engine(db_url)
    session = sessionmaker(bind=db_engine)

    session = session()

    filter_obj = session.query(State).filter(State.id == '2').first()
    filter_obj.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
    update_obj(db_url)
