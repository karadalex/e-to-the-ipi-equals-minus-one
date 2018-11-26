import unittest
# from max_product import findMaxProduct2 as findMaxProduct
from max_product import findMaxProduct2 as findMaxProduct

class TestProducts(unittest.TestCase):

    def test_case1(self):
        numberFile = open("number.txt", "r")
        numberString = ""
        for line in numberFile:
            numberString += line
        numberString = numberString.replace("\n", "")
        res = findMaxProduct(numberString, 4)

        self.assertEquals(res, 5832)

    # Test case with non-zero digits
    def test_case2(self):
        numberFile = open("number2.txt", "r")
        numberString = ""
        for line in numberFile:
            numberString += line
        numberString = numberString.replace("\n", "")
        res = findMaxProduct(numberString, 4)

        # max product is 9 x 9 x 9 x 9 = 6561
        self.assertEquals(res, 6561)

if __name__ == '__main__':
    unittest.main()