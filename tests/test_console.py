#!/usr/bin/python3

""" test the console files """
from console import HBNBCommand
from models.engine.file_storage import FileStorage

import unittest


class TestConsole(unittest.TestCase):
    """ test the console files """
    def setUp(self):
        self.instance = HBNBCommand()
        self.storage = FileStorage()

    def test_create_with_underscores(self):
        """ test do create with params """
        self.instance.do_create("State name='Ekiti_state'")
        result = (self.storage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertEqual(result["name"], "Ekiti state")

    def test_integer(self):
        """ test do create with params """
        self.instance.do_create("State population=233200302")
        result = (self.storage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], int)

    def test_negative_integer(self):
        """ test do create with params """
        self.instance.do_create("State population=-233200302")
        result = (self.storage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], int)

    def test_negative_float(self):
        """ test do create with params """
        self.instance.do_create("State population=-233.200302")
        result = (self.storage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], float)

    def test_float(self):
        """ test do create with params """
        self.instance.do_create("State population=233.200302")
        result = (self.storage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["population"], float)

    def test_negative_float(self):
        """ test do create with params """
        self.instance.do_create('State resort_center=king"s')
        result = (self.storage.all())
        for k, v in result.items():
            result = v.to_dict()
        self.assertTrue(result["resort_center"], "king\"s")
