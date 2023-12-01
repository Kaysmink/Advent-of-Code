Input= open("data/Day 17. input.txt", "r").read().strip().split(":", 1)

x,y = Input[1].strip().split(", ")
minX, maxX = list(map(int,x[2:].split("..")))
minY, maxY = list(map(int,y[2:].split("..")))

def calculateTrajectory(xn, yn):
    x = y = 0
    
    points = [[x,y]] 
    while True:
        x = x + xn
        y = y + yn
        
        points.append([x,y])
        if xn >0:
            xn = xn -1
        yn = yn - 1
        
        if minX<=x<= maxX and minY<=y<=maxY:
            return [True, points]
        if x > maxX or y < minY:
            return [False, points]

def getMaxY(points):
    return max(map(lambda x: x[1], points))

def getpossibleVelocyties():
    possibleVel = []
    highestY = 0 
    for xn in range(1,maxX+1):
        for yn in range(minY,200):
            found, points = calculateTrajectory(xn,yn)
            if found:
                possibleVel.append([xn,yn])
                highestYPoints = getMaxY(points)
                if highestYPoints > highestY:
                    highestY = highestYPoints
    print(highestY)
    print(len(possibleVel))
                
getpossibleVelocyties()
