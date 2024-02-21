#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """ getter attributes that returns the list of City instances with state_id """
        from models import storage
        from models.city import City
        cities = {}
        data = storage.all(City)
        for key, value in data.items():
            if key['state_id'] == self.id:
                cities.update({key: value})


