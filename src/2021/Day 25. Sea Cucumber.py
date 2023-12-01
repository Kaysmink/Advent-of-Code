from copy import deepcopy

Input = open("data/Day 25. input.txt", "r").read().split("\n")[:-1]
positions = [list(line) for line in Input]

def getPositions(direction, positions):
    coords = [[x,y] for x in range(0,len(positions[0])) for y in range(0,len(positions)) if positions[y][x] == direction]
    return coords

def haveNeighbor(x,y, direction, positions):
    maxX = len(positions[0])-1
    maxY = len(positions)-1
    
    if direction == ">":
        neighbor = positions[y][x+1] if x < maxX else positions[y][0]
    if direction == "v":
        neighbor = positions[y+1][x] if y < maxY else positions[0][x]
        
    if neighbor != ".":
        return False
    return True
    
def moveEast(positions):
    global numMoved
    maxX = len(positions[0])-1
    
    coords = getPositions(">", positions)
    canMove = [haveNeighbor(x, y, ">", positions) for x,y in coords]
    numMoved = numMoved + sum(canMove)
    for index, move in enumerate(canMove):
        if move:
            x,y = coords[index]
            positions[y][x] = "."
            if x < maxX:
                positions[y][x+1] = ">"
            else:
                positions[y][0] = ">"
    return positions

def moveSouth(positions):
    global numMoved
    maxY = len(positions)-1
    
    coords = getPositions("v", positions)
    canMove = [haveNeighbor(x, y, "v", positions) for x,y in coords]
    numMoved = numMoved + sum(canMove)
    for index, move in enumerate(canMove):
        if move:
            x,y = coords[index]
            positions[y][x] = "."
            
            if y < maxY:
                positions[y+1][x] = "v"
            else:
                positions[0][x] = "v"
                
    return positions

def step(positions):
    global numMoved
    numMoved = 0
    newPosition = deepcopy(positions)
    newPosition = moveEast(newPosition)
    newPosition = moveSouth(newPosition)
    
    return newPosition

iteration = 0  
while True:
    iteration +=1
    positions = step(positions)
    if numMoved == 0:
        print(iteration)
        break
    