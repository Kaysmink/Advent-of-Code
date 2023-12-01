import copy

Input=open("data/Day 11. input.txt", "r").read().split("\n")[:-1]
Input = [ line.split() for line in Input]

for i in range(0,len(Input)):
    Input[i] = list(Input[i][0])

def checkEmptyToFullPart1(x, y, seats):
    possible = True
    seatsToCheck = [[x-1,y-1], [x,y-1], [x+1,y-1], [x+1,y], [x+1, y+1], [x,y+1], [x-1,y+1], [x-1,y]]
    for x, y in seatsToCheck:
        if x < 0 or y < 0 or x > len(Input[1]) -1 or y > len(Input) -1:
            continue
        if(seats[y][x] == "#"):
            possible = False
            break
    return possible
    

def checkFullToEmptyPart1(x, y, seats): 
    counter = 0 
    seatsToCheck = [[x-1,y-1], [x,y-1], [x+1,y-1], [x+1,y], [x+1, y+1], [x,y+1], [x-1,y+1], [x-1,y]]
    for x, y in seatsToCheck:
        if x < 0 or y < 0 or x > len(Input[1]) -1 or y > len(Input) -1:
            continue
        if(seats[y][x] == "#"):
            counter = counter + 1
    if counter >=4:
        return True
    return False
    
def closestSeat(x,y,direction, sitation):
    if direction == "left":
        x = x - 1
        
        if x < 0:
            return "NA"
                
        while sitation[y][x] == ".":
            x = x - 1
            
            if x < 0:
                return "NA"
        return [x,y]
    
    if direction == "right":
        x = x + 1
        
        if x > len(sitation[1]) -1:
            return "NA"
        
        while sitation[y][x] == ".":
            x = x + 1
            if x > len(sitation[1]) -1:
                return "NA"
        return [x,y]
    
    if direction == "top":
        y = y -1
        
        if y < 0:
            return "NA"
        
        while sitation[y][x] == ".":
            y = y -1
            if y < 0:
                return "NA"
        return [x,y]
    
    if direction == "down":
        y = y + 1
        
        if y > len(sitation) -1:
                return "NA"
            
        while sitation[y][x] == ".":
            y = y + 1
            if y > len(sitation) -1:
                return "NA"
        return [x,y]
    
    if direction == "topleftDiag":
        x = x - 1
        y = y - 1 
        
        if x < 0 or y < 0:
                return "NA"
            
        while sitation[y][x] == ".":
            x = x - 1
            y = y - 1 
            
            if x < 0 or y < 0:
                return "NA"
        return [x,y]
    
    if direction == "toprightDiag":
        x = x + 1
        y = y - 1 
        
        if x > len(sitation[1]) -1 or y < 0:
                return "NA"
            
        while sitation[y][x] == ".":
            x = x + 1
            y = y - 1 
            
            if x > len(sitation[1]) -1 or y < 0:
                return "NA"
        return [x,y]
    
    if direction == "downleftDiag":
        x = x - 1
        y = y + 1 
        
        if x < 0 or y > len(sitation) -1:
                return "NA"
            
        while sitation[y][x] == ".":
            x = x - 1
            y = y + 1  
            
            if x < 0 or y > len(sitation) -1:
                return "NA"
        return [x,y]
    
    if direction == "downrightDiag":
        x = x + 1
        y = y + 1 
        
        if x > len(sitation[1]) -1 or y > len(sitation) -1:
                return "NA"
            
        while sitation[y][x] == ".":
            x = x + 1
            y = y + 1  
            
            if x > len(sitation[1]) -1 or y > len(sitation) -1:
                return "NA"
        return [x,y]
        
def checkEmptyToFullPart2(x, y, seats):
    possible = True
    seatsToCheck = [closestSeat(x,y,"left", seats), 
                    closestSeat(x,y,"right", seats), 
                    closestSeat(x,y,"top", seats), 
                    closestSeat(x,y,"down", seats), 
                    closestSeat(x,y,"topleftDiag", seats), 
                    closestSeat(x,y,"toprightDiag", seats), 
                    closestSeat(x,y,"downleftDiag", seats), 
                    closestSeat(x,y,"downrightDiag", seats)]    
    seatsToCheck = [x for x in seatsToCheck if x != "NA"]
    for x, y in seatsToCheck:
        if(seats[y][x] == "#"):
            possible = False
            break
    return possible

def checkFullToEmptyPart2(x, y, seats): 
    counter = 0 
    seatsToCheck = [closestSeat(x,y,"left", seats), 
                    closestSeat(x,y,"right", seats), 
                    closestSeat(x,y,"top", seats), 
                    closestSeat(x,y,"down", seats), 
                    closestSeat(x,y,"topleftDiag", seats), 
                    closestSeat(x,y,"toprightDiag", seats), 
                    closestSeat(x,y,"downleftDiag", seats), 
                    closestSeat(x,y,"downrightDiag", seats)]
    seatsToCheck = [x for x in seatsToCheck if x != "NA"]
    for x, y in seatsToCheck:
        if(seats[y][x] == "#"):
           counter = counter + 1
    if counter >=5:
        return True
    return False

# deel 1        
situation = copy.deepcopy(Input)
iteration = 0

while True: 
    oldSituation = copy.deepcopy(situation)
    iteration = iteration + 1
    
    counter  = 0 
    for y in range(0, len(oldSituation)):
        for x in range(0,len(oldSituation[1])):
            if situation[y][x] == ".":
                continue
            if situation[y][x] == "L":
                if checkEmptyToFullPart1(x,y,oldSituation):
                    situation[y][x] = "#"
                    counter  = counter + 1
            if situation[y][x] == "#":
                if checkFullToEmptyPart1(x,y,oldSituation):
                    situation[y][x] = "L"
                    counter  = counter + 1
    if counter == 0:
        break
    
print(sum([List.count("#") for List in situation]))

# deel 2 
situation = copy.deepcopy(Input)
iteration = 0

while True: 
    oldSituation = copy.deepcopy(situation)
    iteration = iteration + 1
    
    counter  = 0 
    for y in range(0, len(oldSituation)):
        for x in range(0,len(oldSituation[1])):
            if situation[y][x] == ".":
                continue
            if situation[y][x] == "L":
                if checkEmptyToFullPart2(x,y,oldSituation):
                    situation[y][x] = "#"
                    counter  = counter + 1
            if situation[y][x] == "#":
                if checkFullToEmptyPart2(x,y,oldSituation):
                    situation[y][x] = "L"
                    counter  = counter + 1
    if counter == 0:
        break
    
print(sum([List.count("#") for List in situation]))
