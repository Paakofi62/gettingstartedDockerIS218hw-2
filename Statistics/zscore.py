from MathOperations.subtraction import Subtraction
from MathOperations.division import Division
from Statistics.mean import Mean
from Statistics.stddev import StdDev


class Zscore:
    def zscore(data):
        for num in data:
            z = Subtraction(num, Mean)
            zc = Division(z, StdDev)
        return zc
