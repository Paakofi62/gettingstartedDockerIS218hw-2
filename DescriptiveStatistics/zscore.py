from MathOperations.subtraction import Subtraction
from MathOperations.division import Division
from DescriptiveStatistics.mean import Mean
from DescriptiveStatistics.stddev import Stddev


class Zscore:

    def zscore(data):
        z = Subtraction(data, Mean)
        zc = Division(z, Stddev)
        return zc
