from RandomNumberGenerator.randPick import RandPick


class PopulationProportion:
    @staticmethod
    def populationPorportion(seeds, nums, data):
        p = RandPick.randPickListSeed(seeds, nums, data)
        pp = len(p) / len(data)
        return pp
