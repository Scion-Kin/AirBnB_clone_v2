import unittest
from console import HBNBCommand

class test_console(unittest.TestCase):

    def setUp(self):
        self.new_instance = HBNBCommand()

    def tearDown(self):
        del self.new_instance

    def test_float(self):
        options = {"height": "123.4"}
        self.new_instance.create("State")
        self.new_instance.__dict__.update(options)
        self.assertIsInstance(self.new_instance.__dict__["height"], float)


    def test_float(self):
        options = {"population": 12300000}
        self.new_instance.create("State")
        self.new_instance.__dict__.update(options)
        self.assertIsInstance(self.new_instance.__dict__["height"], int)


    def test_quotes_and_underscore(self):
        options = {"region": 'Western_"Region'}
        self.new_instance.create("State")
        self.new_instance.__dict__.update(options)
        self.assertEqual(self.new_instance.__dict__["region"], 'Western \"Region')

    def test_underscores(self):
        options = {"region": 'Western_Region'}
        self.new_instance.create("State")
        self.new_instance.__dict__.update(options)
        self.assertEqual(self.new_instance.__dict__["region"], 'Western Region')
