from collections import defaultdict
import itertools as it
import copy

Input=open("data/Day 17. input.txt", "r").read().split("\n")[:-1]

activeDict = defaultdict()

for y in range(0,len(Input)):
    for x in range(0,len(Input[y])):
        if Input[y][x] == "#":
            index = ",".join(["0", "0", str(y),str(x)])
            activeDict[index] = True

def runCycle3D(cycle, activeDict):
    newActiveDict = copy.deepcopy(activeDict)
    maxX = startX + cycle
    maxY = startY + cycle
    maxZ = cycle
    
    for x in range(-cycle, maxX+1):
        for y in range(-cycle, maxY+1):
            for z in range(-maxZ, maxZ+1):
                possibleNeighbors = [[x-1, x, x+1], [y-1, y, y+1], [z-1, z, z+1]]
                neighbors = list(it.product(*possibleNeighbors))
                neighbors = [[0, zn, yn, xn] for xn, yn, zn in neighbors if abs(zn) <= maxZ and yn <= maxY and yn >= -cycle and xn <= maxX and xn >= -cycle]
                neighbors.remove([0,z,y,x])
                countActiveNeighbors = 0 
                for wn, zn, yn,xn in neighbors:
                    indexOfNeighbor = ",".join(list(map(str, [wn, zn, yn,xn])))
                    if indexOfNeighbor in activeDict.keys():
                            countActiveNeighbors = countActiveNeighbors +1
                
                index = ",".join(list(map(str, [0, z, y, x])))
                if index in activeDict.keys():
                    if countActiveNeighbors not in [2,3]:
                        newActiveDict[index] = False
                else: 
                    if countActiveNeighbors == 3:
                        newActiveDict[index] = True
    
    deleteInactiveTiles = [key for key, value in newActiveDict.items() if value == False]
    for key in deleteInactiveTiles:
        del newActiveDict[key]
        
    return newActiveDict

def runCycle4D(cycle, activeDict):
    newActiveDict = copy.deepcopy(activeDict)
    maxX = startX + cycle
    maxY = startY + cycle
    maxZ = cycle
    maxW = cycle
    
    for x in range(-cycle, maxX+1):
        for y in range(-cycle, maxY+1):
            for z in range(-maxZ, maxZ+1):
                for w in range(-maxW, maxW+1):
                    possibleNeighbors = [[x-1, x, x+1], [y-1, y, y+1], [z-1, z, z+1], [w-1, w, w+1]]
                    neighbors = list(it.product(*possibleNeighbors))
                    neighbors = [[wn, zn, yn, xn] for xn, yn, zn, wn in neighbors if abs(wn) <= maxW and abs(zn) <= maxZ and yn <= maxY and yn >= -cycle and xn <= maxX and xn >= -cycle]
                    neighbors.remove([w,z,y,x])
                    countActiveNeighbors = 0 
                    for wn, zn, yn,xn in neighbors:
                        indexOfNeighbor = ",".join(list(map(str, [wn, zn, yn,xn])))
                        if indexOfNeighbor in activeDict.keys():
                                countActiveNeighbors = countActiveNeighbors +1
                    
                    index = ",".join(list(map(str, [w, z, y, x])))
                    if index in activeDict.keys():
                        if countActiveNeighbors not in [2,3]:
                            newActiveDict[index] = False
                    else: 
                        if countActiveNeighbors == 3:
                            newActiveDict[index] = True
    
    deleteInactiveTiles = [key for key, value in newActiveDict.items() if value == False]
    for key in deleteInactiveTiles:
        del newActiveDict[key]
        
    return newActiveDict

startX = len(Input[0])
startY = len(Input)
startZ = 0
startW = 0 

activeDict3D = copy.deepcopy(activeDict)
activeDict4D = copy.deepcopy(activeDict)

for cycle in range(1,7):
    activeDict3D = runCycle3D(cycle, activeDict3D)
    activeDict4D = runCycle4D(cycle, activeDict4D)
    
print(len(list(activeDict3D.keys())))
print(len(list(activeDict4D.keys())))
    
