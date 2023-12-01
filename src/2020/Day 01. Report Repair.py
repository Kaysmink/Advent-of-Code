import itertools as it
import numpy as np

Input=open("data/Day 01. input.txt", "r").read().split("\n")
Input=list(map(int, Input))

# deel 1 
for value in Input:
    if 2020 - value in Input:
        print(value * (2020-value))
        break
    
# deel 2
for combination in it.combinations(Input, 3):
    if sum(combination) == 2020:
        print(np.product(combination))