Input = open("data/Day 11. input.txt", "r").read().split("\n")[:-1]
energyLevels = [list(map(int,list(line))) for line in Input]

def findNeighbors(x,y):
    return [[xn, yn] for xn in range(x-1,x+2) for yn in range(y-1,y+2) if 0<=xn<len(Input[0]) and 0<=yn<len(Input) and (abs(x-xn) + abs(y-yn) > 0)]

def nextStep(energyLevels):
    global numOfFlashes
    energyLevels = [[level + 1 for level in line] for line in energyLevels]
    
    flashed = [[[x,y] for x, value in enumerate(lineIndex) if value >9] for y, lineIndex in enumerate(energyLevels)]
    flashed = [coord for line in flashed for coord in line]
    
    for flash in flashed:
        indexNeighbors = findNeighbors(flash[0], flash[1])
        for neighbor in indexNeighbors:
            newValue = energyLevels[neighbor[1]][neighbor[0]] + 1
            energyLevels[neighbor[1]][neighbor[0]] = newValue
            if newValue > 9 and neighbor not in flashed:
                flashed.append(neighbor)
            
    numOfFlashes = numOfFlashes + len(flashed)    
        
    for coord in flashed:
         energyLevels[coord[1]][coord[0]] = 0
    
    if len(flashed) == len(Input)**2:
        return [True, energyLevels]
    
    return [False, energyLevels]

# Deel 1 / Deel 2 
numOfFlashes = 0 
day = 0 

while True:
    day = day + 1
    allFlashes, energyLevels = nextStep(energyLevels)
    if day == 100:
        print(numOfFlashes)
    if allFlashes:
        print(day)
        break
    