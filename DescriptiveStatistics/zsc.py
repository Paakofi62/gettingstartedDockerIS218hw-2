from DescriptiveStatistics.mean import Mean
from DescriptiveStatistics.stddev import Stddev
from MathOperations.subtraction import Subtraction
from MathOperations.division import Division


class Zsc:
    @staticmethod
    def zsc(data):
        z = Subtraction.difference(data, Mean.mean(data))
        zs = Division.division(z, Stddev.stddev(data))
        return zs
