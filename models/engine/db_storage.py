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
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


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
            # Drop all tables if environment is a test env
            meta = Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ qeury storage based on class """
        classes_list = [User, Place, State, City, Amenity, Review]
        temp = {}
        if cls is not None and cls in classes_list:
            results = self.__session.query(cls).all()
            for result in results:
                """ we need to append the class name with the id, this
                is because currently it is [Class] (id): {classObject}
                """
                key = "[{}] ({})".format(result.__class__.__name__, result.id)
                value = result
                temp.update({key: value})
            return temp
        else:
            for clas in classes_list:
                results = self.__session.query(clas).all()
                if results is not None:
                    for result in results:
                        key = "[{}] ({})".format(result.__class__.__name__,
                                                 result.id)
                        value = result
                        temp.update({key: value})
            return temp

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' Creates all database objects '''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
