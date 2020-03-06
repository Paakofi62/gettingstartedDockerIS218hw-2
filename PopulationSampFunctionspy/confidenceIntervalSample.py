from PopulationSampFunctionspy.confidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSampFunctionspy.simpleRandSamp import SimpleRandSamp


class ConfidenceIntervalSample:
    @staticmethod
    def confidenceIntervalSample(confidence, seed, nums, data):
        samp = SimpleRandSamp.randPickListSeed(seed, nums, data)
        return ConfidenceIntervalPopulation.confidenceIntervalPopulation(confidence, samp)
