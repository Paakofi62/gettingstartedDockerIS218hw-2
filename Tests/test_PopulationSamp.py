import unittest
import random
from PopulationSampFunctionspy.marginOfError import MarginOfError


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(2)
        self.test = random.randint(0, 40, 8)

    def test_marginOfError(self):
        result = MarginOfError.marginOfError(2, self.test)
        self.assertEqual(result, 1.33)


if __name__ == '__main__':
    unittest.main()
