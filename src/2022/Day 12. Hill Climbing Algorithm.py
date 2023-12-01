import copy
import math

Input = open("data/dag 12. input.txt", "r").read().split("\n")[:-1]
heights = [list(line) for line in Input]
start = [[x,y] for y in range(0,len(heights)) for x in range(0,len(heights[0])) if heights[y][x] == "S"][0]
end = [[x,y] for y in range(0,len(heights)) for x in range(0,len(heights[0])) if heights[y][x] == "E"][0]
heights = [[ord(char)-96 for char in list(line)] for line in Input]
heights[start[1]][start[0]] = 1
heights[end[1]][end[0]] = 26
poss_startpoints = [[x,y] for y in range(0,len(heights)) for x in range(0,len(heights[0])) if heights[y][x] == 1]


def shortesPath(start, end):
    posRoutes = [[start]]

    checked_points = []
    steps = 0
    while True:
        steps = steps + 1
        # if no routes possible return inf
        if posRoutes == []:
            return math.inf
        newPosRoutes = []
        for route in posRoutes:
            currentPos = route[-1]
            currentHeight = heights[currentPos[1]][currentPos[0]]
            neighbors = [[xn, yn] for xn in range(currentPos[0]-1, currentPos[0]+2) for yn in range(currentPos[1]-1, currentPos[1]+2) if currentPos[0] == xn or currentPos[1] == yn]
            
            for neighbor in neighbors:
                # check if new neighbor already in route, or if neighbor is another point with height 1
                # if this is the case than we can discard this neighbor since there always will be a shorter path possible
                if neighbor in route:
                    continue
                if neighbor in already_checked:
                    continue
                x, y = neighbor
                # discard neighbor if out of bounds
                if x <0 or x >= len(Input[0]) or y<0 or y>=len(heights):
                    continue
                
                height = heights[y][x]
                if height <= currentHeight +1:
                    # check if neighbor already checked in another route
                    # if this is the case we can discard this neighbor since there always be shorter path possible
                    if neighbor not in checked_points:
                        checked_points.append(neighbor)
                        newRoute = copy.deepcopy(route)
                        newRoute.append(neighbor)
                        newPosRoutes.append(newRoute)
                        if neighbor == end:
                            return steps
        posRoutes = newPosRoutes

# Deel 1
already_checked = []
print(shortesPath(start, end))

# Deel 2
result = math.inf 
for index, point in enumerate(poss_startpoints):
    already_checked.append(point)
    value = shortesPath(point, end)
    if value < result:
        result = value
print(result)
    

