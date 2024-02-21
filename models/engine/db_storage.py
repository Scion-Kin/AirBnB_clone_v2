#!/usr/bun/python3


import os
import sqlalchemy
from sqlalchemy import create_engine, MetaData, URL
from sqlalchemy.orm import sessionmaker, scoped_session

from ..base_model import Base
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..user import User
from ..review import Review
from .. state import State


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        url_object = URL.create(
            "mysql+mysqldb",
            username=user,
            password=pwd,
            host=host,
            database=db,
            query={"charset": "utf8"}
        )
        self.__engine = create_engine(url_object, pool_pre_ping=True)
        if env == "test" or "Test":
            MetaData.drop_all()

    def all(self, cls=None):
        """ retrieves data based on the class name"""
        session = self.__session
        return_obj = {}
        if cls:
            classes = ["User", "Place", "Review", "Amenity", "State", "City"]
            class_name = str(type(cls).split('.')[-1].split('\'')[0])
            if class_name in classes:
                result = session.query(cls).all()
                for obj in result:
                    return_obj[obj.id] = obj
            return return_obj
        else:
            result = session.query().all()
            for obj in result:
                return_obj[obj.id] = obj
            return return_obj

    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
