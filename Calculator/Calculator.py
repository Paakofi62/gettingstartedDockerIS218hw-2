from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponential import Exponential
from MathOperations.squareroot import SquareRoot
from MathOperations.logarithm import Logarithm


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiplication(self, a, b):
        self.Result = Multiplication.multiplication(a, b)
        return self.Result

    def Division(self, a, b):
        self.Result = Division.division(a, b)
        return self.Result

    def Exponential(self, a, b):
        self.Result = Exponential.exponential(a, b)
        return self.Result

    def SqaureRoot(self, a, b):
        self.Result = SquareRoot.squareroot(a, b)
        return self.Result

    def Logarithm(self, a, b):
        self.Result = Logarithm.logarithm(a, b)
        return self.Result
