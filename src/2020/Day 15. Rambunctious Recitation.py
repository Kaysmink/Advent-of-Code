from collections import defaultdict

Input=open("data/Day 15. input.txt", "r").read().split(",")
Input = list(map(int, Input))

turn = 0
saidNumbers = defaultdict(list)
spoken = Input[-1]

for value in Input: 
    turn = turn + 1
    saidNumbers[value].append(turn)
    
while True:
    turn = turn + 1 
    lastNumber = spoken
    firstTime =  len(saidNumbers[lastNumber]) == 1
    if firstTime:
        spoken = 0
    else: 
       spoken =  saidNumbers[lastNumber][1] - saidNumbers[lastNumber][0]
    if len(saidNumbers[spoken]) < 2:
        saidNumbers[spoken].append(turn)
    else:
        saidNumbers[spoken][0] = saidNumbers[spoken][1]
        saidNumbers[spoken][1] = turn 
    # deel 1 
    if turn == 2020:
        print(spoken)
    # deel 2, runtime 1 minute 
    if turn == 30000000:
        print(spoken)
        break
       
       
      

