from DescriptiveStatistics.covariance import Covariance
from DescriptiveStatistics.stddev import Stddev


class PopulationCorrelation:
    @staticmethod
    def populationcorrelation(data1, data2):
        cov = Covariance.covariance(data1, data2)
        stdDev1 = Stddev.stddev(data1)
        stdDev2 = Stddev.stddev(data2)
        return cov / (stdDev1 * stdDev2)
