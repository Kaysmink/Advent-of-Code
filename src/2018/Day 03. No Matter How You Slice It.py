from collections import defaultdict

Input=open("data/day 03. input.txt", "r").read().split("\n")[:-1]

listX =  []
listY = []

for claim in Input:
    inchesFromLeft, inchesFromTop = list(map(int,claim.split(" @ ")[1].split(":")[0].split(",")))
    wide, tall = list(map(int,claim.split(" @ ")[1].split(": ")[1].split("x")))
    
    xRange = [inchesFromLeft + 1, inchesFromLeft + wide]
    yRange = [inchesFromTop + 1, inchesFromTop + tall]
    
    listX.append(xRange)
    listY.append(yRange)

matrixDict = defaultdict(list)
claimNumber = 0
listOfClaimes = defaultdict()
for indexX, indexY in zip(listX, listY):
    claimNumber = claimNumber + 1
    listOfClaimes[claimNumber] = True
    for x in range(indexX[0], indexX[1] +1 ):
        for y in range(indexY[0], indexY[1] + 1):
            key = str(x) + "-" + str(y)
            matrixDict[key].append(claimNumber)

# deel 1 
print(len([List for List in matrixDict.values() if len(List) > 1]))

# deel 2 
for key, value in matrixDict.items():
    if(len(value) > 1):
        for claimnumber in value:
            listOfClaimes[claimnumber] = False

for key, value in listOfClaimes.items():
    if value == True:
        print(key)
        break
