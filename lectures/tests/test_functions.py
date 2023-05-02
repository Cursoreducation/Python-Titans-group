from functions import *
import unittest
from unittest import mock


class FunctionsTest(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 4), 9)
        self.assertEqual(suma(3, 2), 5)
        with self.assertRaises(TypeError):
            suma(5, "2")

    def test_diff(self):
        self.assertEqual(diff(5, 4), 1)
        self.assertEqual(diff(4, 8), -4)

    def test_div(self):
        self.assertEqual(div(4, 2), 2)
        self.assertEqual(div(6, 2), 3)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_mn(self):
        self.assertEqual(mn(5, 2), 10)
        self.assertEqual(mn(4, 3), 12)

    def test_suma_with_rand(self):
        with mock.patch("functions.rand", return_value=5):
            self.assertEqual(suma_with_rand(5, 4), 14)