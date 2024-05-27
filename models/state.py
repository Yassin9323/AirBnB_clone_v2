#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship(
            "City", cascade='all, delete, delete-orphan', backref="state"
            )
    else:
        @property
        def cities(self):
            """ Getter for FileStorage Mode """
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
