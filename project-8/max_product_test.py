import unittest
from max_product import findMaxProduct1 as findMaxProduct

class TestProducts(unittest.TestCase):

    def test_case1(self):
        numberFile = open("number.txt", "r")
        numberString = ""
        for line in numberFile:
            numberString += line
        numberString = numberString.replace("\n", "")
        res = findMaxProduct(numberString, 4)

        self.assertEquals(res, 5832)

if __name__ == '__main__':
    unittest.main()