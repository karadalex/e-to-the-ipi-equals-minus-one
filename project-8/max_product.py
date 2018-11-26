import sys

"""
First solution
num: digits in string form
r:   lenght/range of each product group
"""
def findMaxProduct1(num, r):
    maxProduct = 0
    for i in range(len(num)-r):
        product = 1
        for j in range(i, i+r):
            product = product * int(num[j])
        
        if product > maxProduct:
            maxProduct = product

    return maxProduct

"""
Second solution
num: digits in string form
r:   lenght/range of each product group
"""
def findMaxProduct2(num, r):
    maxProduct = 0
    product = 1
    # Assume that first digit is non-zero
    for i in range(r):
        product = product * int(num[i])

    i = 1
    while i < len(num)-r:
        print(product)
        product = int(product/int(num[i-1]))
        product = product * int(num[i+r])
        print(product)
        if product > maxProduct:
            maxProduct = product
        
        i += 1

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
    
    print(findMaxProduct2(numberString, groupLength))