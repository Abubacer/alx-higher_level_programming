#!/usr/bin/python3
"""
Defines the City class and an instance of Base.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Represent a City class that inherits from Base.

    Attributes:
        __tablename__ (str): The class city table name.
        id (int): The class city id.
        name (str): The class city name.
        state_id (int): The state in which the city located.
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
