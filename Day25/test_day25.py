import unittest
from day25 import Snafu, Decimal


class TestSnafu(unittest.TestCase):

    def test_one(self):
        number = Snafu('1')
        self.assertEqual(number.decimal, 1)

    def test_3(self):
        number = Snafu('1=')
        self.assertEqual(number.decimal, 3)

    def test_2022(self):
        number = Snafu('1=11-2')
        self.assertEqual(number.decimal, 2022)
    
    def test_4890(self):
        number = Snafu('2=-1=0')
        self.assertEqual(number.decimal, 4890)


class TestDecimal(unittest.TestCase):

    def test_one(self):
        number = Decimal(1)
        self.assertEqual(number.snafu, '1')
    
    def test_2022(self):
        number = Decimal(2022)
        self.assertEqual(number.snafu, '1=11-2')

    def test_4890(self):
        number = Decimal(4890)
        self.assertEqual(number.snafu, '2=-1=0')
