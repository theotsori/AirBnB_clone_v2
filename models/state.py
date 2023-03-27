#!/usr/bin/python3
"""This is the state module."""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This class defines a state."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """
            getter attribute that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            cities = storage.all('City')
            cities_list = []
            for city in cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
