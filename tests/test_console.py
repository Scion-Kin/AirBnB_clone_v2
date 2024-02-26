#!/usr/bin/python3

""" test the console files """
from console import HBNBCommand
# from models.engine.file_storage import FileStorage
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


import unittest


class TestConsole(unittest.TestCase):
    """ test the console files """
    def setUp(self):
        self.inst = HBNBCommand()
        self.fsstorage = FileStorage()
        self.dbstorage = DBStorage()

    def test_create_with_underscores(self):
        """ test do create with params """
        self.inst.do_create("State name='Ekiti_state'")
        result = (self.fsstorage.all(State))
        for k, v in result.items():
            result = v.to_dict()
        self.assertEqual(result["name"], "Ekiti state")

    def test_integer(self):
        """ test do create with params """
        self.inst.do_create("State name='Ekiti_state' population=233200302")
        result = (self.fsstorage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], int)

    def test_negative_integer(self):
        """ test do create with params """
        self.inst.do_create("State name='Ekiti_state' population=-233200302")
        result = (self.fsstorage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], int)

    def test_negative_float(self):
        """ test do create with params """
        self.inst.do_create("State name='Ekiti_state' population=-233.200302")
        result = (self.fsstorage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], float)

    def test_float(self):
        """ test do create with params """
        self.inst.do_create("State name='Ekiti_state' population=233.200302")
        result = self.fsstorage.all()
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], float)

    def test_negative_float(self):
        """ test do create with params """
        self.inst.do_create('State name="Ekiti_state" resort_center=king"s')
        result = self.fsstorage.all()
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["resort_center"], "king\"s")
