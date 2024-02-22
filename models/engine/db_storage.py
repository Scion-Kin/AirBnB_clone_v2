#!/usr/bin/python3
"""Sql database storage engine"""

from os import getenv
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Class defining a storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        '''Initializes the storage enginge'''
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        if (getenv('HBNB_ENV') == 'test'):
            # Drop all tables if environment is a test one

            all = self.__session.query(Tables).all()

            del all

            self.__session.commit()

    def all(self, cls=None):
        if cls.__name__ is not None:
            every = self.__session.query(cls.__name__).all()

            # Make and return a dict like in FileStorage

        else:
            every = self.__session.query(Tables).all()

            # Make and return a dict like in FileStorage

    def new(self, obj):
        self.all().update(obj.to_dict())

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            del self.all[obj.name]

    def reload(self):
        ''' Creates all database objects '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(scoped_session, bind=self.__engine,
                               expire_on_commit=False)
        self.__session = Session()
