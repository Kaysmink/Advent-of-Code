import math

Input= open("data/Day 16. input.txt", "r").read().strip()
binary = bin(int("1" + Input, 16))[3:]

def parseLiteral(package):
    binNumber = "" 
    while package[0] == "1":
        binNumber = binNumber + package[1:5]
        package = package[5:]
    binNumber = binNumber + package[1:5]
    package = package[5:]

    literalValue = int(binNumber,2)
    return literalValue, package


def parseBinary(package):
    global sumOfVersion
    
    version, typeID = int(package[:3], 2), int(package[3:6], 2)
    sumOfVersion = sumOfVersion + version
    package =  package[6:]
    
    literalValue = 0
    if typeID == 4:
        literalValue, package = parseLiteral(package)
        
    if typeID != 4:
        lengthID = int(package[0], 2)
        package = package[1:]
         
        literalsInOperator = []
    
        if lengthID == 0:    
            L = int(package[0:15],2)
            package = package[15:]
            child = package[:L]
            package = package[L:]
            while child:
                childValue, child = parseBinary(child)
                literalsInOperator.append(childValue)
                 
        else:
            numOfChilds = int(package[:11], 2)
            package = package[11:]
            for x in range(numOfChilds):
                childValue, package = parseBinary(package)
                literalsInOperator.append(childValue)
        
        if typeID == 0:
            literalValue = sum(literalsInOperator)
        if typeID == 1:
            literalValue = math.prod(literalsInOperator)
        if typeID == 2:
            literalValue = min(literalsInOperator)
        if typeID == 3:
            literalValue = max(literalsInOperator)
        if typeID == 5:
            literalValue = 1 if literalsInOperator[0] > literalsInOperator[1] else 0
        if typeID == 6:
            literalValue = 1 if literalsInOperator[0] < literalsInOperator[1] else 0
        if typeID == 7:
            literalValue = 1 if literalsInOperator[0] == literalsInOperator[1] else 0
    
    return literalValue, package
    
sumOfVersion = 0
result = parseBinary(binary)
print(sumOfVersion)       
print(result[0])
    
