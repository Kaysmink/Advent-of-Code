from collections import defaultdict
from collections import Counter

Input=open("data/day 06. input.txt", "r").read().split("\n")[:-1]

def closest_coordinate(x,y, coordinates):
    distances = [abs(int(xCord)-x) + abs(int(yCord)-y) for xCord, yCord in coordinates]
    closestCoordinate = distances.index(min(distances))
    
    return closestCoordinate

def sumOfDistances(x,y, coordinates):
    distances = [abs(int(xCord)-x) + abs(int(yCord)-y) for xCord, yCord in coordinates]
    totalDistance = sum(distances)
    
    if totalDistance < 10000:
        return True
    
    return False
    
coordinates = [line.split(", ") for line in Input]
maxX = max([int(x) for x,y in coordinates])
maxY = max([int(y) for x,y in coordinates])

infiniteClosest = defaultdict(str)
closest = defaultdict(str)
safeCoordinates = defaultdict(bool)

extremeValue = 1
for x in range(-extremeValue, maxX+extremeValue +1):
    for y in range(-extremeValue, maxY+extremeValue +1):
        index = str(x) + "," + str(y)
        closest[index] = closest_coordinate(x, y, coordinates)
        
        # check which coordinates are closest to extreme cases so that we know these are infinite coordinates
        if x == -extremeValue or x == maxX+extremeValue or y == -extremeValue or y == maxY+extremeValue:
            infiniteClosest[index] = closest_coordinate(x, y, coordinates)

        if sumOfDistances(x, y, coordinates):
            safeCoordinates[index] = True

infiniteCoords = list(Counter(infiniteClosest.values()).keys())
countClosest = Counter(closest.values())
nonInfinite = [[key, value] for key, value in countClosest.items() if key not in infiniteCoords]

# deel 1 en 2 
print(max(map(lambda x: x[1], nonInfinite)))
print(len(safeCoordinates.items()))

