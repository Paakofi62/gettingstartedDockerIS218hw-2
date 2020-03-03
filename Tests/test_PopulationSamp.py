import unittest
import random
from PopulationSampFunctionspy.marginOfError import MarginOfError
from PopulationSampFunctionspy.sysSamp import SysSamp


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [1, 2, 2, 2, 3, 4, 5, 5]
        self.test1 = [1, 2, 3, 3, 4, 5, 7, 8]
        random.seed(2)

    def test_marginOfError(self):
        result = MarginOfError.marginOfError(2, self.test)
        self.assertEqual(result, -2.0)




if __name__ == '__main__':
    unittest.main()
