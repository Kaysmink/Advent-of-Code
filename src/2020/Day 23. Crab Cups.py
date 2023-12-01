from collections import deque
import time

Input = list(map(int,list(open("data/Day 23. input.txt", "r").read())))
#Input = list(map(int,list("389125467")))

def find_destination(arrangement, current, exclude):
    newNum = current-1
    
    while True:
        if newNum < 1:
            newNum = maxNum
            continue
        if newNum not in exclude:
            return newNum
        newNum = newNum -1
        
def play_move(arrangement):
    current = arrangement[0]
    arrangement.rotate(-1)
    pickThree = [arrangement.popleft(), arrangement.popleft(), arrangement.popleft()]
    pickThree = pickThree[::-1]
    
    destination = find_destination(arrangement, current, pickThree)
    
    indexNewCurrent = arrangement.index(destination)
    arrangement.rotate(-indexNewCurrent-1)
    arrangement.extendleft(pickThree)
    
    arrangement.rotate(-arrangement.index(current)-1)
    
    return arrangement
   
def play_crabs(arrangement, numOfTurns):
    for i in range(numOfTurns):
        arrangement = play_move(arrangement)
    return arrangement
    
def part_1():
    arrangement = deque(Input)
    numOfTurns = 100
    
    start = time.time()
    arrangement = play_crabs(arrangement, numOfTurns)
    print("play_crabs = ", time.time()-start)
    
    arrangement.rotate(-arrangement.index(1))
    print("".join(list(map(str,list(arrangement)))[1:]))

def part_2():
    global maxNum 

    arrangement = Input + [i for i in range(max(Input)+1, 1000000)]
    arrangement = deque(arrangement)
    
    maxNum = max(arrangement)
    numOfTurns = 100
    
    start = time.time()
    arrangement = play_crabs(arrangement, numOfTurns)
    print("play_crabs = ", time.time()-start)
    
    arrangement.rotate(-arrangement.index(1)-1)
    print(arrangement.popleft() * arrangement.popleft())

maxNum = 9 
part_1()
part_2()