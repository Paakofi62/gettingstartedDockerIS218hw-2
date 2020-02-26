import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponential import Exponential
from MathOperations.squareroot import SquareRoot
from MathOperations.logarithm import Logarithm


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_multiplication(self):
        self.assertEqual(2, Multiplication.multiplication(1, 2))

    def test_MathOperations_division(self):
        self.assertEqual(2, Division.division(4, 2))

    def test_MathOperations_exponential(self):
        self.assertEqual(27, Exponential.exponential(3, 3))

    def test_MathOperations_root(self):
        self.assertEqual(6, SquareRoot.squareroot(36, 2))

    def test_MathOperations_Logarithm(self):
        self.assertEqual(3, Logarithm.logarithm(64, 4))


if __name__ == '__main__':
    unittest.main()
