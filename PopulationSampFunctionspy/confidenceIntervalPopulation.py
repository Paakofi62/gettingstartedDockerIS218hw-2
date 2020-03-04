from scipy.stats import sem
from scipy.stats import t
from DescriptiveStatistics.mean import Mean


class ConfidenceIntervalPopulation:
    @staticmethod
    def confidenceIntervalPopulation(confidence, data):
        ll = len(data)
        md = Mean.mean(data)
        stder = sem(data)
        h = stder * t.ppf((1 + confidence) / 2, ll - 1)
        beginInterval = md - h
        endInterval = md + h
        return beginInterval, endInterval
