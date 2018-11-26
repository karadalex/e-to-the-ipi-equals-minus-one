import sys

"""
num: digits in string form
r:   lenght/range of each product group
"""
def findMaxProduct(num, r):
    maxProduct = 0
    for i in range(len(num)-r):
        product = 1
        for j in range(i, i+r):
            product = product * int(num[j])
        
        if product > maxProduct:
            maxProduct = product

    return maxProduct

if __name__ == '__main__':
    # Load file with a big number
    numberFile = open(sys.argv[1], "r")
    # Convert number to a string of digits
    numberString = ""
    for line in numberFile:
        numberString += line
    numberString = numberString.replace("\n", "")
    groupLength = int(sys.argv[2])
    
    print(findMaxProduct(numberString, groupLength))