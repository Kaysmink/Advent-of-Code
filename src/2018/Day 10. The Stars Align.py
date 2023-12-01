# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 13:43:42 2021

@author: kaysm
"""

from collections import defaultdict
from copy import deepcopy
import pandas as pd

Input=open("data/day 10. input.txt", "r").read().split("\n")[:-1]
#Input=open("data/sample.txt", "r").read().split("\n")

def addSecond(positions):
    newPositions = defaultdict()
    
    for index, position in positions.items():
        newX = position[0] + velocity[index][0]
        newY = position[1] + velocity[index][1]
        newPositions[index] = [newX, newY]
        
    return newPositions

def noNeighbors(positions):
    numOfBadStars = 0 
    for position in positions.values():
        xPos, yPos = position
        numOfNeighbors = 0
        for x in range(xPos-1,xPos+2):
            for y in range(yPos-1,yPos+2):
                if x == xPos and y == yPos:
                    continue
                if [x,y] in positions.values():
                    numOfNeighbors = numOfNeighbors + 1             
        if numOfNeighbors == 0:
            numOfBadStars = numOfBadStars + 1

    if numOfBadStars > 3:
        return True
    
    return False

def printPositions(positions):
    maxX = max([x for x,y in positions.values()])
    minX = min([x for x,y in positions.values()])
    maxY = max([y for x,y in positions.values()])
    minY = min([y for x,y in positions.values()])
    
    matrix = [deepcopy([""])*(maxX+1)]*(maxY+1)
    matrix = [deepcopy(line) for line in matrix]

    for x,y in positions.values():
        matrix[y][x] = "*"
        
    matrix = matrix[minY:]
    matrix = [line[minX:] for line in matrix]
    
    pandasMatrix = pd.DataFrame(data=matrix)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    pd.set_option('display.width', 500)
    print(pandasMatrix)
        
        
velocity = defaultdict()
positions = defaultdict()

for index, line in enumerate(Input):
    position = list(map(int,line.split("<")[1].split(">")[0].split(", ")))
    velo = list(map(int,line.split("velocity=<")[1][:-1].split(", ")))
    
    velocity[index] = velo
    positions[index] = position
    

iteration = 0
while noNeighbors(positions):
    iteration = iteration + 1
    positions = addSecond(positions)
    
# Deel 1 
printPositions(positions)

# Deel 2
print(iteration)
