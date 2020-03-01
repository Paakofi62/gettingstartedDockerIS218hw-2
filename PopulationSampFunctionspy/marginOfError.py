from DescriptiveStatistics.stddev import Stddev
from DescriptiveStatistics.zsc import Zsc


class MarginOfError:
    @staticmethod
    def marginOfError(seed, data):
        zsc = Zsc.zsc(seed, data)
        stddev = Stddev.stddev(data)
        return zsc * stddev
