import unittest
import random
from DescriptiveStatistics.mean import Mean
from DescriptiveStatistics.meanDeviation import MeanDeviation
from DescriptiveStatistics.mode import Mode
from DescriptiveStatistics.skewness import Skewness
from DescriptiveStatistics.stddev import Stddev
from DescriptiveStatistics.variance import Variance
from DescriptiveStatistics.quartiles import Quartiles
from DescriptiveStatistics.median import Median
from DescriptiveStatistics.zsc import Zsc


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 2, 2, 3, 4, 5, 5]
        random.seed(2)

    def test_Mean(self):
        self.assertEqual(3, Mean.mean(self.test))

    def test_mode(self):
        self.assertEqual(2, Mode.mode(self.test))

    def test_median(self):
        self.assertEqual(2.5, Median.median(self.test))

    def test_Variance(self):
        self.assertEqual(2, Variance.variance(self.test))

    def test_stddev(self):
        self.assertEqual(1.5118578920369088, Stddev.stddev(self.test))

    def test_quartile1(self):
        self.assertEqual(2, Quartiles.firstquartile(self.test))

    def test_quartile2(self):
        self.assertEqual(2.5, Quartiles.secondquartile(self.test))

    def test_quartile3(self):
        self.assertEqual(4.25, Quartiles.thirdquartile(self.test))

    def test_zsc(self):
        zsc = Zsc.zsc(2, self.test)
        self.assertEqual(zsc, -1.3228756555322954)

    def test_meanDeviation(self):
        self.assertEqual(1.25, MeanDeviation.meanDeviation(self.test))

    def test_modeskewness(self):
        self.assertEqual(.6614378277661477, Skewness.modeskewness(self.test))

    def test_medianskewness(self):
        self.assertEqual(.33071891388307384, Skewness.medianskewness(self.test))


if __name__ == '__main__':
    unittest.main()
