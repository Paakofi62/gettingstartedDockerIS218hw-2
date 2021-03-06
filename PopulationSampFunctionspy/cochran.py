from DescriptiveStatistics.zsc import Zsc
from PopulationSampFunctionspy.marginOfError import MarginOfError
from DescriptiveStatistics.populationProportion import PopulationProportion
from MathOperations.exponential import Exponential
from MathOperations.subtraction import Subtraction


class Cochran:
    @staticmethod
    def cochran(data, seeds, nums):
        ZScore = Zsc.zsc(seeds,data)
        pp = PopulationProportion.populationPorportion(seeds, nums, data)
        MarOfError = MarginOfError.marginOfError(seeds, data)
        sub = Subtraction.difference(1, pp)
        cochran = (Exponential.exponential(ZScore, 2) * pp * sub) / Exponential.exponential(MarOfError, 2)
        return cochran


obj = Cochran.cochran([1,2,3], 3, 2)
print(obj)

