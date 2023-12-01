from collections import deque

Input = list(map(int,list(open("data/Day 23. input.txt", "r").read())))
Input = list(map(int,list("389125467")))

arrangement = deque(Input)

def find_destination(arrangement, current):
    minNumber = min(arrangement)

    newNum = current-1
    while True:
        if newNum < minNumber:
            newNum = max(arrangement)
            continue
        if newNum in arrangement:
            return newNum
        newNum = newNum -1
        
def play_move(arrangement, ):
    current = arrangement[0]
    arrangement.rotate(-1)
    pickThree = [arrangement.popleft(), arrangement.popleft(), arrangement.popleft()]
    pickThree = pickThree[::-1]

    destination = find_destination(arrangement, current)
    indexNewCurrent = arrangement.index(destination)
    arrangement.rotate(-indexNewCurrent)

    arrangement.rotate(-1)
    arrangement.extendleft(pickThree)
    
    arrangement.rotate(-arrangement.index(current))
    arrangement.rotate(-1)
    
    return arrangement
    

numOfTurns = 100
for i in range(numOfTurns):
    arrangement = play_move(arrangement)
    print(arrangement)
    
arrangement.rotate(-arrangement.index(1))
"".join(list(map(str,list(arrangement)))[1:])
