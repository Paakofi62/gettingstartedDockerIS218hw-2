from RandomNumberGenerator.randomNum import RandomNum


class RandomList:

    @staticmethod
    def randomList(length, seed, x, y):
        data = []
        while len(data) != length:
            data.append(RandomNum.randomNumSeed(seed, x, y))
        return data
