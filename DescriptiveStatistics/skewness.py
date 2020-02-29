from DescriptiveStatistics.mean import Mean
from DescriptiveStatistics.mode import Mode
from DescriptiveStatistics.median import Median
from DescriptiveStatistics.stddev import Stddev
from MathOperations.division import Division
from MathOperations.subtraction import Subtraction


class Skewness:

    @staticmethod
    def modeskewness(data):
        n = (Subtraction.difference(Mean, Mode))
        nn = Division.division(n, Stddev)
        return nn

    @staticmethod
    def medianskewness(data):
        ni = (Subtraction.difference(Mean, Median))
        nii = Division.division(ni, Stddev)
        return nii
