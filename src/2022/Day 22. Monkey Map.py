import re
from itertools import cycle

Input = open("data/dag 22. input.txt", "r").read().split("\n\n")

board = [list(line) for line in Input[0].split("\n")]
walls = [[x,y] for y in range(len(board)) for x in range(len(board[y])) if board[y][x] == "#"]
freeSpace = [[x,y] for y in range(len(board)) for x in range(len(board[y])) if board[y][x] == "."]
path_numbers = list(map(int,re.findall(r'\d+', Input[1])))
path_directions = re.findall(r'[A-Z]', Input[1])

new_dir_dict = {"R":{"R":"D", "L":"U"}, "L":{"R":"U", "L":"D"}, "U":{"R":"R", "L":"L"}, "D":{"R":"L", "L":"R"}}
dir_dict = {"R":0, "D":1, "L":2, "U":3}
parameters_dict = {"R": "(index, maxValue, minValue, 1)", "L":"(index, maxValue, minValue, -1)", "U":"(indexY, maxValue, minValue, -1)","D":"(indexY, maxValue, minValue, 1)"}
minMax_parameters = {"R": "minMaxRow[indexY]", "L":"minMaxRow[indexY]", "U":"minMaxCol[index]", "D":"minMaxCol[index]"}

# Min and max for each row and column
minMaxRow = [[[value != " " for value in board[index]].index(True), len(board[index]) - 1] for index in range(len(board))]
cols = [[" " if index >= len(board[y]) else board[y][index] for y in range(len(board))] for index in range(150)]
minMaxCol = [[[value != " " for value in col].index(True), len(col) -1 if " " not in col else len(col) - [value == " " for value in col[::-1]].index(False) - 1] for col in cols]

def possible_indexes(index, maxValue, minValue, direction):
    if direction == 1:
        possible_index = list(range(index+1, maxValue+1))
        possible_index.extend(list(range(minValue, index+1)))
    
    if direction == -1:
        possible_index = list(range(index-1, minValue-1, -1))
        possible_index.extend(list(range(maxValue, index-1, -1)))
        
    cycle_list = cycle(possible_index)
    indexes = [next(cycle_list) for value in range(steps)]
    
    return indexes

def get_new_pos(indexes, currentPos, direction):
    if direction in ["R", "L"]:
        for index, value in enumerate(indexes):
            if [value, currentPos[1]] in walls:
                new_pos = currentPos if index == 0 else [indexes[index-1], currentPos[1]]
                break
        else:
            new_pos = [indexes[-1], currentPos[1]]
            
    if direction in ["U", "D"]:
        for index, value in enumerate(indexes):
            if [currentPos[0], value] in walls:
                new_pos = currentPos if index == 0 else [currentPos[0], indexes[index-1]]
                break
        else:
            new_pos = [currentPos[0],indexes[-1]]
        
    return new_pos

def find_new_position(direction, steps):
    index, indexY = currentPos
    minValue, maxValue = eval(minMax_parameters[currentDir])
    
    indexes = possible_indexes(*eval(parameters_dict[currentDir]))
    new_pos = get_new_pos(indexes, currentPos, currentDir)

    return new_pos

currentPos = freeSpace[0]
currentDir = "R"

while path_numbers:
    steps = path_numbers.pop(0)
    currentPos = find_new_position(currentDir, steps)
    if not path_directions:
        break

    currentDir = new_dir_dict[currentDir][path_directions.pop(0)]

print(((currentPos[1] + 1) * 1000) + (4*(currentPos[0] + 1)) + dir_dict[currentDir])
