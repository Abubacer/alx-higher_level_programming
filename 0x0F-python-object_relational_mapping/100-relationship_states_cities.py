#!/usr/bin/python3
"""
This is a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_obj(db_url):
    """
    Creates the State “California” with the City “San Francisco”.
    """
    db_engine = create_engine(db_url)
    Base.metadata.create_all(db_engine)
    session = sessionmaker(bind=db_engine)

    session = session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
    create_obj(db_url)
