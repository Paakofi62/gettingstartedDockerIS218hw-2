import numpy as np


class Quartiles:

    @staticmethod
    def firstquartile(data):
        q1 = np.percentile(data, [25])
        return q1

    @staticmethod
    def secondquartile(data):
        q2 = np.percentile(data, [50])
        return q2

    @staticmethod
    def thirdquartile(data):
        q3 = np.percentile(data, [75])
        return q3
