import numpy


class Covariance:
    @staticmethod
    def covariance(X_value, Y_value):
        return numpy.cov(X_value, Y_value)[0, 1]
