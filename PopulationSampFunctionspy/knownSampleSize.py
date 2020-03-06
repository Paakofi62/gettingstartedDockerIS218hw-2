from DescriptiveStatistics.zsc import Zsc
from PopulationSampFunctionspy.marginOfError import MarginOfError
from DescriptiveStatistics.stddev import Stddev
from MathOperations.exponential import Exponential


class KnownSampleSize:
    @staticmethod
    def knownSamplesize(seed, data):
        z = Zsc.zsc(seed, data)
        Mar = MarginOfError.marginOfError(seed, data)
        StDe = Stddev.stddev(data)
        value = (z * StDe) / Mar
        sam = Exponential.exponential(value, 2)
        return sam
