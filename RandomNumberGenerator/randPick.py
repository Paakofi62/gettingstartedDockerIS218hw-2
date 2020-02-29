import random

class RandPick:
    @staticmethod
    def randPick(data):
        return random.choice(data)

    @staticmethod
    def randPickSeed(seed, data):
        random.seed(seed)
        return RandPick.randPick(data)

    @staticmethod
    def randPickList(nums, data):
        dlist = []
        while len(dlist) < nums:
            dlist.append(RandPick.randPick(data))
        return dlist

    @staticmethod
    def ranPickListSeed(seed, nums, data):
        random.seed(seed)
        return RandPick.randPickList(nums, data)