import unittest
import random
from PopulationSampFunctionspy.marginOfError import MarginOfError
from PopulationSampFunctionspy.sysSamp import SysSamp
from PopulationSampFunctionspy.confidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSampFunctionspy.simpleRandSamp import SimpleRandSamp
from PopulationSampFunctionspy.cochran import Cochran
from PopulationSampFunctionspy.confidenceIntervalSample import ConfidenceIntervalSample
from PopulationSampFunctionspy.unknownPopulationStdev import UnknownPopulationStdev
from PopulationSampFunctionspy.knownSampleSize import KnownSampleSize


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [1, 2, 2, 2, 3, 4, 5, 5]
        self.test1 = [1, 2, 3, 3, 4, 5, 7, 8]
        random.seed(2)

    def test_marginOfError(self):
        result = MarginOfError.marginOfError(2, self.test)
        self.assertEqual(result, -2.0)

    def test_confidenceIntervalPopulation(self):
        result = ConfidenceIntervalPopulation.confidenceIntervalPopulation(confidence=.90, data=self.test)
        self.assertEqual(result, (1.9873051382212144, 4.012694861778786))

    def test_confidenceIntervalSample(self):
        result = ConfidenceIntervalSample.confidenceIntervalSample(confidence=.90, seed=1, nums=5, data=self.test1)
        self.assertEqual(result, (1.426075892772384, 6.173924107227616))

    def test_unknownPopulationStdev(self):
        result = UnknownPopulationStdev.unknownPopulationStdev(seed=1, data=self.test1, percent=.50)
        self.assertEqual(result, 0.04281345565749235)

    def test_knownSampleSize(self):
        result = KnownSampleSize.knownSamplesize(seed=4, data=self.test1)
        self.assertEqual(result, 1)

    def test_simpleRandSamp(self):
        result = SimpleRandSamp.randPickList(nums=3, data=self.test1)
        self.assertEqual(result, [1, 2, 2])

    def test_sysSamp(self):
        result = SysSamp.randPickListSeed(seed=1, nums=4, data=self.test1)
        self.assertEqual(result, [3, 2, 4, 2])

    def test_knownSamplesize(self):
        result = KnownSampleSize.knownSamplesize(data=self.test1, seed=1)
        self.assertEqual(result, 1)

    def test_cochran(self):
        result = Cochran.cochran(data=self.test1, seeds=1, nums=4)
        self.assertEqual(result, 0.04281345565749235)


if __name__ == '__main__':
    unittest.main()
