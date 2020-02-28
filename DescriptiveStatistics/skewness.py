from DescriptiveStatistics.mean import Mean
from DescriptiveStatistics.mode import Mode
from DescriptiveStatistics.median import Median
from DescriptiveStatistics.stddev import Stddev
from MathOperations.division import Division
from MathOperations.subtraction import Subtraction


class Skewness:

    @staticmethod
    def modeskewness(data):
        n = (Subtraction(Mean, Mode))
        nn = Division(n, Stddev)
        return nn

    @staticmethod
    def medianskewness(data):
        ni = (Subtraction(Mean, Median))
        nii = Division(ni, Stddev)
        return nii
