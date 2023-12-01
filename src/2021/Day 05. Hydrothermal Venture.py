from collections import defaultdict

Input = open("data/Day 05. input.txt", "r").read().split("\n")[:-1]
coordinates = [[number.split(",") for number in coord.split(" -> ")] for coord in Input]

def getAnswer(part):
    numOfLinesPerCoord = defaultdict(int)
    for coord in coordinates:
        x1, y1, x2, y2 = [int(number) for List in coord for number in List]

        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                newCoord = str(x1) + "," + str(i)
                numOfLinesPerCoord[newCoord] +=1
            
        elif y1 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                newCoord = str(i) + "," + str(y1) 
                numOfLinesPerCoord[newCoord] +=1
        
        else:
            if part == "part2":
                if abs(x1-x2) == abs(y1-y2):
                    for x,y in zip(range(x1,x2, 1 if x2>x1 else -1), range(y1,y2, 1 if y2>y1 else -1)):
                        newCoord = str(x) + "," + str(y) 
                        numOfLinesPerCoord[newCoord] +=1
                        
                    numOfLinesPerCoord[str(x2) + "," + str(y2)] +=1
            else:
                pass
    
    return sum(value >= 2 for value in numOfLinesPerCoord.values())

print(getAnswer("part1"))
print(getAnswer("part2"))
    