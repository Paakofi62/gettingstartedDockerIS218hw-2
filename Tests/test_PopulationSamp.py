import unittest
import random
from PopulationSampFunctionspy.marginOfError import MarginOfError
from PopulationSampFunctionspy.sysSamp import SysSamp
from PopulationSampFunctionspy.confidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSampFunctionspy.simpleRandSamp import SimpleRandSamp


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

    def test_simpleRandSamp(self):
        result = SimpleRandSamp.randPickList(nums=3, data=self.test1)
        self.assertEqual(result, [1, 2, 2])

    def test_sysSamp(self):
        result = SysSamp.randPickListSeed(seed=1, nums=4, data=self.test1)
        self.assertEqual(result, [3, 2, 4, 2])


if __name__ == '__main__':
    unittest.main()
