from collections import defaultdict
from collections import deque
import copy

Input = open("data/Day 24. input.txt", "r").read().split("\n")[:-1]

coordDict = {"e": [0,2], 
             "w": [0,-2], 
             "se": [-1,1],
             "sw": [-1,-1], 
             "ne": [1,1], 
             "nw": [1,-1]}

instructions = []
for line in Input:
    instruction = []

    line = deque(list(line))
    while line:    
        if line[0] in coordDict.keys():
            instruction.append(line.popleft())
        else:
            instr = line.popleft() + line.popleft()
            instruction.append(instr)
    instructions.append(instruction)

# deel 1 
flippedDict = defaultdict(int)    
for instruction in instructions:
    coordinates = [0,0]
    for direction in instruction:
        coordinates[0] = coordinates[0] + coordDict[direction][0]
        coordinates[1] = coordinates[1] + coordDict[direction][1]
    
    index = ",".join(list(map(str,coordinates))) 
    flippedDict[index] =  flippedDict[index] + 1

blackSide = [key for key, value in flippedDict.items() if value%2 == 1]
print(len(blackSide))

# Deel 2
def runDay(day, blackDict):
    newBlackDict = copy.deepcopy(blackDict)
    maxX = startX + (day + 1)*2
    maxY = startY + day + 2
    
    for x in range(-maxX, maxX+1):
        for y in range(-maxY, maxY+1):
            neighbors = [[y, x+2], [y, x-2], [y+1, x+1], [y+1, x-1], [y-1, x+1], [y-1, x-1]]
            neighbors = [[yn, xn] for yn, xn in neighbors if abs(yn) <= maxY and abs(xn) <= maxX]

            countblackNeighbors = 0 
            for yn,xn in neighbors:
                indexOfNeighbor = ",".join(list(map(str, [yn,xn])))
                if indexOfNeighbor in blackDict.keys():
                        countblackNeighbors = countblackNeighbors +1
            
            index = ",".join(list(map(str, [y,x])))
            if index in blackDict.keys():
                if countblackNeighbors == 0 or countblackNeighbors > 2:
                    newBlackDict[index] = False
            else: 
                if countblackNeighbors == 2:
                    newBlackDict[index] = True
    
    deleteWhiteTiles = [key for key, value in newBlackDict.items() if value == False]
    for key in deleteWhiteTiles:
        del newBlackDict[key]
        
    return newBlackDict
        
blackDict = defaultdict()
for value in blackSide:
    blackDict[value] = True

startY = 0 
startX = 0
for value in blackSide:
    y, x = value.split(",")
    if abs(int(y)) > startY:
        startY = int(y)
    if abs(int(x)) > startX:
        startX = int(x)
        
day = 1
while day <= 100:
    blackDict = runDay(day, blackDict)
    day = day + 1

print(len(blackDict.keys()))