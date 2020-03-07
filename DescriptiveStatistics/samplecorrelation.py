from DescriptiveStatistics.stddev import Stddev
from RandomNumberGenerator.randPick import RandPick
from DescriptiveStatistics.covariance import Covariance


class SampleCorrelation:
    @staticmethod
    def samplecorrelation(seed, sample_size, data1, data2):
        dataA = RandPick.randPickListSeed(seed, sample_size, data1)
        dataB = RandPick.randPickListSeed(seed, sample_size, data2)

        return Covariance.covariance(dataA, dataB) / (Stddev.stddev(dataA) * Stddev.stddev(dataB))
