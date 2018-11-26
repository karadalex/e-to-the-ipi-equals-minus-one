import sys


groupLength = int(sys.argv[1])
# Load file with a big number
numberFile = open("number.txt", "r")

# Convert number to a string of digits
numberString = ""
for line in numberFile:
    numberString += line
numberString = numberString.replace("\n", "")

maxProduct = 0
for i in range(len(numberString)-groupLength):
    product = 1
    for j in range(i, i+groupLength):
        product = product * int(numberString[j])
    
    if product > maxProduct:
        maxProduct = product

print(maxProduct)