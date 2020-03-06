from MathOperations.exponential import Exponential
from MathOperations.division import Division
from MathOperations.subtraction import Subtraction
from DescriptiveStatistics.zsc import Zsc
from PopulationSampFunctionspy.marginOfError import MarginOfError


class UnknownPopulationStdev:
    @staticmethod
    def unknownPopulationStdev(seed, data, percent):
        ZScore = Zsc.zsc(seed, data)
        MarOfError = MarginOfError.marginOfError(seed, data)
        p = percent
        q = Subtraction.difference(1, p)
        pq = Division.division(ZScore, MarOfError)
        samplePopulation = Exponential.exponential(pq, 2) * p * q

        return samplePopulation
