from collections import defaultdict
import itertools as it
import copy

Input=open("data/Day 14. input.txt", "r").read().split("\n")[:-1]
Input = [instruction.split(" = ") for instruction in Input]

# deel 1 
mask = ""
mem = defaultdict(int)

for instruction, value in Input: 
    if instruction == "mask":
        mask = list(value)
    else: 
        index = instruction.split("[")[1][:-1]
        binair = list(f'{int(value):036b}')
        result =copy.copy(binair)
        for i in range(0,len(mask)):
            if mask[i] != "X":
                result[i] = mask[i]
        result = int("".join(result),2)
        mem[index] = result

print(sum(mem.values()))
    
# deel 2
mask = ""
mem = defaultdict(int)

for instruction, value in Input:
    combinationsOfFloatingPoints = []
    possibleIndexes = []
    if instruction == "mask":
        mask = list(value)
    else: 
        index = instruction.split("[")[1][:-1]
        binair = list(f'{int(index):036b}')
        result =copy.copy(binair)
        for i in range(0,len(mask)):
            if mask[i] != "0":
                result[i] = mask[i]
        for perm in it.product([0,1], repeat = result.count("X")):
            combinationsOfFloatingPoints.append(list(perm))
        for combinations in combinationsOfFloatingPoints:
            combination = copy.copy(result)
            for i in range(0,len(result)):
                if result[i] == "X":
                    combination[i] = str(combinations.pop())     
            possibleIndexes.append("".join(combination))
        possibleIndexes = [int("".join(index),2) for index in possibleIndexes]
        for index in possibleIndexes:
            mem[index] = int(value)
            
print(sum(mem.values()))

