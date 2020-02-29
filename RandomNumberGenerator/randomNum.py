import random


class RandomNum:
    @staticmethod
    def randomNum(x, y):
        return random.randint(x, y)

    @staticmethod
    def randomNumSeed(seed, x, y):
        random.seed(seed)
        return RandomNum.randomNum(x, y)
