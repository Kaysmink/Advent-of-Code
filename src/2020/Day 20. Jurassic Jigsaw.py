from collections import defaultdict
import math
import numpy as np 
import pandas as pd

Input=open("data/Day 20. input.txt", "r").read().split("\n\n")[:-1]
Input=open("data/test.txt", "r").read().split("\n\n")

dimension = int(len(Input)**0.5)
def readInput():
    tileDict = defaultdict()
    for tile in Input:
        key, tile = tile.split("\n",1)
        key = int(key.replace("Tile ", "").replace(":", ""))
        tile = [list(line) for line in tile.split("\n")]
        tileDict[key] = tile
    return tileDict

def getBorders():
    bordersDict = defaultdict()
    for key, tile in tileDict.items():
        borders = defaultdict()
        top = tile[0]
        down = tile[-1]
        
        left = []
        right = []
        
        for y in range(0,len(tile)):
            left.append(tile[y][0])
            right.append(tile[y][-1])
        
        borders["top"] = top
        borders["down"] = down
        borders["left"] = left
        borders["right"] = right
        
        borders["reverse top"] = top[::-1]
        borders["reverse down"] = down[::-1]
        borders["reverse left"] = left[::-1]
        borders["reverse right"] = right[::-1]
        
        bordersDict[key] = borders
        
    return bordersDict

def getPossibleNeighbors():
    possNeighbors = defaultdict(list)
    for tile, value in bordersDict.items():
        numOfNeighbors = 0
        for tile2, value2 in bordersDict.items():
            if tile == tile2:
                continue
            for orientation, border in value.items():
                for orientation2, border2 in value2.items():
                    if border == border2:
                        possNeighbors[tile].append([tile2, [orientation, orientation2]])
                        numOfNeighbors = numOfNeighbors + 1
    return possNeighbors

def degreesOfSeperation(Tile):
    degrees = defaultdict()
    degrees[Tile] = 0
    
    while len(degrees.keys()) < len(Input):
        for tile, neighbors in PossibleNeighborsDict.items():
            possibleSteps = []
            for tile2, neighbor in neighbors:
                if tile2 in degrees.keys():
                    possibleSteps.append(degrees[tile2] + 1)
            if len(possibleSteps) != 0:
                if tile in degrees.keys():
                    degrees[tile] = min(min(possibleSteps), degrees[tile])
                else:
                    degrees[tile] = min(possibleSteps)
    return degrees

def addListToColumn(listToAdd, colNum):
    for i in range(0,len(listToAdd)):
        tileArrangement[i][colNum] = listToAdd[i]

def inMatrix(tile):
    for line in tileArrangement:
        if tile in line:
            return True
    return False

def addAllTiles():
    for y in range(1,dimension-1):
        for x in range(1,dimension-1):
            neighbors = [tileArrangement[y][x-1], tileArrangement[y-1][x]]
            tileToAdd = [tile for tile in degreesOfSeperation(neighbors[0]).keys() if (degreesOfSeperation(neighbors[0])[tile] == 1 and degreesOfSeperation(neighbors[1])[tile] == 1 and inMatrix(tile) == False)]
            print(tileToAdd)
            tileToAdd = tileToAdd[0]
            tileArrangement[y][x] = tileToAdd
            
        
# Deel 1 
tileDict = readInput()
bordersDict =  getBorders()  
PossibleNeighborsDict = getPossibleNeighbors() 

corners = []
sides = []
center = []
for tile, neighbors in PossibleNeighborsDict.items():
    if len(neighbors) == 4:
        corners.append(tile)
    if len(neighbors) == 6:
        sides.append(tile)
    if len(neighbors) == 8:
        center.append(tile)

print(math.prod(corners))

# deel 2
tileArrangement = [["NA"] *dimension]*dimension
tileArrangement = [line.copy() for line in tileArrangement]

cornerDegrees = defaultdict()
for corner in corners:
    cornerDegrees[corner] = degreesOfSeperation(corner)

# 1747-1811
# 2347-2281

# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
side1747a1811 = [[tile for tile in cornerDegrees[1951].keys() if (cornerDegrees[1951][tile] == i and cornerDegrees[3079][tile] == dimension-1-i)] for i in range(0,dimension)]
side1811a2281 = [[tile for tile in cornerDegrees[3079].keys() if (cornerDegrees[3079][tile] == i and cornerDegrees[1171][tile] == dimension-1-i)] for i in range(0,dimension)]
side2347a2281 = [[tile for tile in cornerDegrees[2971].keys() if (cornerDegrees[2971][tile] == i and cornerDegrees[1171][tile] == dimension-1-i)] for i in range(0,dimension)]
side1747a2347 = [[tile for tile in cornerDegrees[1951].keys() if (cornerDegrees[1951][tile] == i and cornerDegrees[2971][tile] == dimension-1-i)] for i in range(0,dimension)]

# side1747a1811 = [[tile for tile in cornerDegrees[1747].keys() if (cornerDegrees[1747][tile] == i and cornerDegrees[1811][tile] == dimension-1-i)] for i in range(0,dimension)]
# side1811a2281 = [[tile for tile in cornerDegrees[1811].keys() if (cornerDegrees[1811][tile] == i and cornerDegrees[2281][tile] == dimension-1-i)] for i in range(0,dimension)]
# side2347a2281 = [[tile for tile in cornerDegrees[2347].keys() if (cornerDegrees[2347][tile] == i and cornerDegrees[2281][tile] == dimension-1-i)] for i in range(0,dimension)]
# side1747a2347 = [[tile for tile in cornerDegrees[1747].keys() if (cornerDegrees[1747][tile] == i and cornerDegrees[2347][tile] == dimension-1-i)] for i in range(0,dimension)]

side1747a1811 = [tile[0] for tile in side1747a1811]
side1811a2281 = [tile[0] for tile in side1811a2281]
side2347a2281 = [tile[0] for tile in side2347a2281]
side1747a2347 = [tile[0] for tile in side1747a2347]

tileArrangement[0] = side1747a1811
tileArrangement[dimension-1] = side2347a2281
addListToColumn(side1811a2281, dimension-1)
addListToColumn(side1747a2347, 0)

addAllTiles()

# tilesOrientation = defaultdict()
# test = pd.DataFrame(tileDict[1951])
# print(test)
# print(np.rot90(test, k=1, axes=(1,0)))
# test = np.array(test)
# np.flip(test, axis = 0)

# testList = []
# testList.append(pd.DataFrame(np.flip(test, axis = 0)))





