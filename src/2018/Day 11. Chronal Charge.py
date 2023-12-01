# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:21:43 2021

@author: kaysm
"""

serialNumber=int(open("data/day 11. input.txt", "r").read())

def calculate_power_level(x,y):
    rackId = (x + 10) 
    return int(str(((rackId*y + serialNumber) * rackId) // 100)[-1]) - 5

def calculate_grid(xPos, yPos, gridSize):
    xBound = min(300, xPos+gridSize)
    yBound = min(300, yPos+gridSize)
    
    return sum([sum([grid[y-1][x-1] for x in range(xPos, xBound)]) for y in range(yPos, yBound)]) 

def make_starting_grid():
    return [[calculate_power_level(x, y) for x in range(1,301)] for y in range(1,301)]
    
def make_grid_gridSize(gridSize):
    bound = 300-gridSize+1
    grid = [[calculate_grid(x, y, gridSize) for x in range(1,bound+1)] for y in range(1,bound+1)]
    return grid

def max_of_grid(grid):
    return max([max(grid[y]) for y in range(0,len(grid))])

def result(grid, maxValue, gridSize):
    for x in range(0,len(grid)):
        for y in range(0, len(grid)):
            if grid[y][x] == maxValue:
                return str(x+1) + "," + str(y+1) + "," + str(gridSize) 
   
grid = make_starting_grid()

# Deel 1 
gridThree = make_grid_gridSize(3)
maxValue = max_of_grid(gridThree)
print(result(gridThree, maxValue, 3)[0:-2])

# Deel 2 
highScore = 0 
bestGridSize = 0 

bestGrid = []
for i in range(1, 10):
    dimGrid = make_grid_gridSize(i)
    maxValue = max_of_grid(dimGrid)
    if maxValue > highScore:
        highScore = maxValue
        bestGridSize = i 
        bestGrid = dimGrid

print(result(bestGrid, highScore, bestGridSize))
    
