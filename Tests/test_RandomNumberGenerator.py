import unittest
from RandomNumberGenerator.randPick import RandPick
from RandomNumberGenerator.randomNum import RandomNum
from RandomNumberGenerator.randomList import RandomList


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5]

    def test_randomNum(self):
        result = RandomNum.randomNum(0, 5)
        self.assertEqual(int, type(result))

    def test_randomNumSeed(self):
        result1 = RandomNum.randomNumSeed(5, 0, 20)
        result2 = RandomNum.randomNumSeed(5, 0, 12)
        self.assertEqual(False, result1 == result2)

    def test_randNumList(self):
        result1 = RandomList.randomList(1, 5, 0, 20)
        result2 = RandomList.randomList(1, 5, 0, 20)
        self.assertEqual(True, result1 == result2)

    def test_randPick(self):
        result = RandPick.randPick(self.test)
        x = None
        if result in self.test and type(result) == int:
            x = True
        self.assertEqual(True, x)

    def test_randPickSeed(self):
        result = RandPick.randPickSeed(4, self.test)
        result2 = RandPick.randPickSeed(2, self.test)
        x = None
        if result in self.test and type(result) == int:
            if result == result2:
                x = True
        self.assertEqual(True, x)

    def test_randPickList(self):
        temp = RandPick.randPickList(4, self.test)
        x = None
        if len(temp) == 4:
            for item in temp:
                if item in self.test and type(item) == int:
                    x = True
        self.assertEqual(True, x)

    def test_randPickListSeed(self):
        temp = RandPick.randPickListSeed(5, 1, self.test)
        temp2 = RandPick.randPickListSeed(5, 1, self.test)
        x = None
        if temp == temp2:
            x = True
        self.assertEqual(True, x)


if __name__ == '__main__':
    unittest.main()
