from DescriptiveStatistics.stddev import Stddev
from RandomNumberGenerator.randomNum import RandomNum
from DescriptiveStatistics.covariance import Covariance


class SampleCorrelation:
    @staticmethod
    def samplecorrelation(Seed, data1, data2):
        sampleData1 = RandomNum.randomNumSeed(Seed, data1, 5)
        sampleData2 = RandomNum.randomNumSeed(Seed, data2, 5)

        cov = Covariance.covariance(sampleData1, sampleData2)
        stdDev1 = Stddev.stddev(sampleData1)
        stdDev2 = Stddev.stddev(sampleData2)
        return cov / (stdDev1 * stdDev2)
