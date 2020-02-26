from MathOperations.addition import Addition
from MathOperations.division import Division
from MathOperations.subtraction import Subtraction
from MathOperations.exponential import Exponential
from Statistics.mean import Mean


class SampVariance:
    def sampvarinace(data):
        sampv = 0
        for num in data:
            s = Subtraction(num, Mean)
            v = Exponential(s, 2)
            a = Addition.sumList(v)
            d = Division(a, Subtraction(num, 1))
            sampv = d
        return sampv
