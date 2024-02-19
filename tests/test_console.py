import unittest
from console import HBNBCommand

class test_console(unittest.TestCase):

    def setUp(self):
        self.new_instance = HBNBCommand()

    def test_float(self):
        options = {"height": "123.4"}
        self.new_instance.create("State")
        self.new_instance.__dict__.update(options)
        self.assertIsInstance(self.new_instance.__dict__["height"], float)

    def test_negative_float(self):
        options = {"balance": "-123.4"}
        self.new_instance.create("User")
        self.new_instance.__dict__.update(options)
        self.assertIsInstance(self.new_instance.__dict__["balance"], float)

    def test_int(self):
        options = {"population": "12312233"}
        self.new_instance.create("State")
        self.new_instance.__dict__.update(options)
        self.assertIsInstance(self.new_instance.__dict__["population"], int)

    def test_negative_int(self):
        options = {"rating": "-3"}
        self.new_instance.create("Review")
        self.new_instance.__dict__.update(options)
        self.assertIsInstance(self.new_instance.__dict__["rating"], int)


