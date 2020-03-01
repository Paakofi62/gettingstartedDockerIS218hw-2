from DescriptiveStatistics.mean import Mean
from DescriptiveStatistics.stddev import Stddev
from RandomNumberGenerator.randPick import RandPick


class Zsc:
    @staticmethod
    def zsc(seed, data):
        X = RandPick.randPickSeed(seed, data)
        mean = Mean.mean(data)
        stddev = Stddev.stddev(data)
        return (X - mean) / stddev
