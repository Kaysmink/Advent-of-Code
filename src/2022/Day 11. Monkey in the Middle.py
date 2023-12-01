import re
import math

Input = open("data/dag 11. input.txt", "r").read().split("\n\n")
priorities = [list(map(int,re.findall(r'\d+', monkey.split("\n")[1]))) for monkey in Input]
operations = [monkey.split("\n")[2].split(" = ")[1] for monkey in Input]
test = [int(re.findall(r'\d+', monkey.split("\n")[3])[0]) for monkey in Input]
newMonkey = [list(map(int,re.findall(r'\d+', monkey)))[-2:] for monkey in Input]

ggd = math.prod(test) # gemeenschappelijke deler
counter = [0 for i in range(0, len(Input))]

def play_round(part):
    for monkey in range(0,len(Input)):
        for old in priorities[monkey]:
            counter[monkey] = counter[monkey] + 1
            new = eval(operations[monkey]) #// 3
            if part == "1":
                new = new //3
            else: 
                # take new%ggd since this will not alter the devisibilty of the numbers 
                new = new%ggd
                
            if new%test[monkey] == 0:
                priorities[newMonkey[monkey][0]].append(new)
            else:
                priorities[newMonkey[monkey][1]].append(new)
        priorities[monkey] = []

def play_rounds(part):
    for roundNum in range(10000):
        play_round(part)
        if part == "1":
            if roundNum == 19:
                break
    
play_rounds("2") 
counter = sorted(counter, reverse = True)
print(counter[0] * counter[1])
