
from os import getenv
import unittest

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database
from models.engine.db_storage import DBStorage
from console import HBNBCommand

user = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
database = getenv('HBNB_MYSQL_DB')

engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
        .format(user, password, host, database),
        pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class TestDbStorage(unittest.TestCase):
    """ Tests storing to sql db """
    def setUp(self):
        """ code to run on every test case"""
        Base.metadata.create_all(engine)
        self.storage = DBStorage()
        self.console = HBNBCommand()

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_state_creation(self):
        """ creates a state instance """
        self.console.do_create("State name='Ekiti_state'")
        result = session.query(State).all()
        self.assertEqual(result[0].name, "Ekiti state")


