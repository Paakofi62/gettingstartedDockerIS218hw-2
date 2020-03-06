from DescriptiveStatistics.zsc import Zsc
from PopulationSampFunctionspy.marginOfError import MarginOfError
from DescriptiveStatistics.populationProportion import PopulationProportion
from MathOperations.exponential import Exponential
from MathOperations.subtraction import Subtraction


class Cochran:
    @staticmethod
    def cochran(data, seeds, nums):
        ZScore = Zsc.zsc(data, seeds)
        pp = PopulationProportion.populationPorportion(data, nums, seeds)
        MarOfError = MarginOfError.marginOfError(data, seeds)
        sub = Subtraction.difference(1, pp)
        cochran = (Exponential.exponential(ZScore, 2) * pp * sub) / Exponential.exponential(MarOfError, 2)
        return cochran
