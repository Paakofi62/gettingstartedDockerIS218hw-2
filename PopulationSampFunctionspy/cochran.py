from DescriptiveStatistics.zsc import Zsc
from PopulationSampFunctionspy.marginOfError import MarginOfError
from DescriptiveStatistics.populationProportion import PopulationProportion
from MathOperations.exponential import Exponential
from MathOperations.subtraction import Subtraction


class Cochran:
    @staticmethod
    def cochran(data, seed, nums):
        ZScore = Zsc.zsc(data, seed)
        pp = PopulationProportion.populationPorportion(data, nums, seed)
        MarOfError = MarginOfError.marginOfError(data, seed)
        sub = Subtraction.difference(1, pp)
        cochran = (Exponential.exponential(ZScore, 2) * pp * sub) / Exponential.exponential(MarOfError, 2)
        return cochran
