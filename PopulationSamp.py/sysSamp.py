from RandomNumberGenerator.randPick import RandPick


class SysSamp(RandPick):

    def sysSamp(self, seed, nums, data):
        return self.ranPickListSeed(seed, nums, data)
