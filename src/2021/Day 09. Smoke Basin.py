Input = open("data/Day 09. input.txt", "r").read().split("\n")[:-1]
Input = [list(map(int, list(line))) for line in Input]

def findNeighbors(x,y):
    neighbors = [Input[yn][xn] for xn in range(x-1,x+2) for yn in range(y-1,y+2) if 0<=xn<len(Input[0]) and 0<=yn<len(Input) and (abs(x-xn) + abs(y-yn) == 1)]
    indexNeighbors = [[xn, yn] for xn in range(x-1,x+2) for yn in range(y-1,y+2) if 0<=xn<len(Input[0]) and 0<=yn<len(Input) and (abs(x-xn) + abs(y-yn) == 1)]
    return neighbors, indexNeighbors

def findLowPoints():
    lowPoints = [[x,y] for y in range(0, len(Input)) for x in range(0, len(Input[0])) if Input[y][x] < min(findNeighbors(x, y)[0])]
    return lowPoints
 
# Deel 1 
lowPoints = findLowPoints()
riskLevel = sum([1+Input[y][x] for x,y in lowPoints])
print(riskLevel)

def checkFlow(lowPoint):
    global flow
    
    x,y = lowPoint
    lowValue = Input[y][x]
    neighbors, indexNeighbors = findNeighbors(x, y)

    flows = [neighbor > lowValue if (neighbor != 9) else False for neighbor in neighbors]
    
    for index, flowing in enumerate(flows):
        if flowing == True:
            if indexNeighbors[index] not in flow:
                flow.append(indexNeighbors[index])
                checkFlow(indexNeighbors[index])

# Deel 2
flowToLowpoint = []
for lowPoint in lowPoints:
    flow = [lowPoint]
    checkFlow(lowPoint)
    flowToLowpoint.append(flow)

sizeOfBasins = sorted([len(basin) for basin in flowToLowpoint], reverse = True)
print(sizeOfBasins[0] * sizeOfBasins[1] * sizeOfBasins[2])
        