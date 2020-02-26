from MathOperations.addition import Addition
from MathOperations.division import Division


class Mean:

    def mean(data):
        num_values = len(data)
        total = 0
        for num in data:
            total = Addition.sum(total, num)
        return Division(total, num_values)
