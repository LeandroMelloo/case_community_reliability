"""
    Sample tests
"""
from django.test import SimpleTestCase

from app import calculator_test


class TestCalculator(SimpleTestCase):
    """ Test the calculator module """

    def test_add(self):
        """ Test the add function """
        self.assertEqual(calculator_test.add(1, 2), 3)

    def test_sub(self):
        """ Test the add function """
        self.assertEqual(calculator_test.sub(5, 2), 3)
