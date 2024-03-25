#!/usr/bin/python3
""" State Module for HBNB project """
from models import FileStorage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    state_id = ''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete")

    '''@property
    def cities(self):
        """
        return city instances with state_id == city.id
        """
        from models.city import City
        local_storage = FileStorage()
        list_instances = []
        results = local_storage.all(City)
        for key, value in results.items():
            if value.state_id == self.id:
                list_instances.append({key: value})
        return list_instances'''
