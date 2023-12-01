# Vast en zeker super inefficient maar kon geen slimmere manier bedenken. 
Input= open("data/Day 18. input.txt", "r").read().split("\n")[:-1]

def IsExploding(line):
    order = OrderLine(line)
    depth = 0 
    for index, char in enumerate(order):
        if char == "[":
            depth +=1
        if char == "]":
            depth -=1
        
        if depth == 5:
            return [True, index]
    return [False, False]

def RemoveBrackets(line):
    removeChars = "[]"
    for char in removeChars:
        line = line.replace(char, "")
        
    return line

def IsSplitting(line):
    line = list(map(int,RemoveBrackets(line).split(",")))
    
    if max(line) >= 10:
        return True
    return False

def OrderLine(line):
    order = []
    double = False
    for index, char in enumerate(line):
        if double == True:
            double = False
            continue
        if char.isnumeric() == False:
            order.append(char)
            double = False
        else:
            if line[index+1].isnumeric():
                order.append(char+line[index+1])
                double = True
            else:
                order.append(char)
                double = False
                
    return order

def findLeftNumber(order, index):
    for i in range(index, -1, -1):
        if order[i].isnumeric():
            return [order[i], i]
        
    return [False, False]

def findRightNumber(order, index):
    for i in range(index, len(order)):
        if order[i].isnumeric():
            return [order[i], i]
        
    return [False, False]
    
def Explode(line, indexExplosion):
    order = OrderLine(line)
    
    endIndex = indexExplosion + order[indexExplosion::].index("]")
    explodingPair = order[indexExplosion+1:endIndex]
    explodingPair = [int(explodingPair[0]), int(explodingPair[2])]

    leftNumber = findLeftNumber(order, indexExplosion)
    if leftNumber[0] == False:
        leftNumber = [-explodingPair[0], indexExplosion+1]

    rightNumber = findRightNumber(order, endIndex)
    if rightNumber[0] == False:
        rightNumber = [-explodingPair[1], len(order)+1]
    
    newOrder = []
    for index, char in enumerate(order):
        if indexExplosion<=index<endIndex:
            continue
        
        if index < leftNumber[1]:
            newOrder.append(char)
        if index == leftNumber[1]:
            newOrder.append(str(int(leftNumber[0]) + explodingPair[0]))
        if index in range(leftNumber[1]+1,indexExplosion):
            newOrder.append(char)
        if index == endIndex:
            newOrder.append("0")
        if endIndex<index<rightNumber[1]:
            newOrder.append(char)
        if index == rightNumber[1]:
            newOrder.append(str(int(rightNumber[0]) + explodingPair[1]))
        if index > rightNumber[1]:
            newOrder.append(char)
        
    newLine = "".join(newOrder)
    
    return newLine
    
def Split(line):
    order = OrderLine(line)
    indexSplit = min([index for index, value in enumerate(order) if value.isnumeric() and int(value) >=10])
    number = int(order[indexSplit])
    newPair = [number//2, number//2+1] if number%2 == 1 else [number//2, number//2]
    
    order[indexSplit] = "[" + str(newPair[0]) + "," + str(newPair[1]) + "]"
    
    newLine = "".join(order)
    
    return newLine
        
def Reduce(line):
    while IsExploding(line)[0] or IsSplitting(line):
        if IsExploding(line)[0]:
            line = Explode(line, IsExploding(line)[1])
            continue
        else:
            line = Split(line)
    return line

def SumAllLines():
    som = Input[0]
    for line in Input[1:]:
        newLine = "[" + som + "," + line + "]"
        reduced = Reduce(newLine)
        som = reduced
    return som

def SumLines(line, line2):
    newLine = "[" + line + "," + line2 + "]"
    reduced = Reduce(newLine)
    som = reduced
    return som

def leftSide(line):
    depth = 0
    for index, char in enumerate(line):
        if char == "[":
            depth +=1
        if char == "]":
            depth -=1
        if depth == 0:
            return index

def Magnitude(line):
    if line.isnumeric():
        return int(line)
    
    else: 
        order = OrderLine(line)
        order = order[1:-1]
        
        endLeft = leftSide(order)
        left = "".join(order[0:endLeft+1])
        right = "".join(order[endLeft+2::])
        return 3*Magnitude(left) + 2*Magnitude(right)

def calculateHighScore():
    highScore = 0 
    for line in Input:
        for line2 in Input:
            if line != line2:
                som = SumLines(line, line2)
                result = Magnitude(som)
                if result > highScore:
                    highScore = result
                    
    return highScore

som = SumAllLines()
print(Magnitude(som))
print(calculateHighScore())


