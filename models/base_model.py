#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime as dt
from sqlalchemy import String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=dt.utcnow())
    updated_at = Column(DateTime, nullable=False, default=dt.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = dt.utcnow()
            self.updated_at = dt.utcnow()
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'updated_at' and 'created_at' in kwargs:
                kwargs['updated_at'] = dt.strptime(kwargs['updated_at'],
                                                   '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = dt.strptime(kwargs['created_at'],
                                                   '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(**kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = dt.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})

        if self.created_at and self.created_at:
            dictionary.update({'created_at': self.created_at.isoformat()})
            dictionary.update({'updated_at': self.created_at.isoformat()})

        else:
            dictionary.update({'created_at': dt.utcnow()})
            dictionary.update({'updated_at': dt.utcnow()})

        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ deletes the instance from memory """
        storage.delete(self)
