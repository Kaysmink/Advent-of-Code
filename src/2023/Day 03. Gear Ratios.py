import regex as re
import numpy as np


def findNeighbors(x, y):
    return [[xn, yn] for xn in range(x-1, x+2) for yn in range(y-1, y+2) if 0 <= xn < len(Input[0]) and 0 <= yn < len(Input) and (abs(x-xn) + abs(y-yn) > 0)]


Input = open("data/2023/dag 03. input.txt", "r").read().split("\n")[0:-1]

# Part 1
number_coords = [[[match.start(), match.end()] for match in re.finditer(r'\d+', line)] for line in Input]
full_number_coords = [[[[y, x] for x in range(xmin, xmax)]
                       for xmin, xmax in number_coords[y]] for y in range(0, len(Input))]
numbers = [[int(match.group()) for match in re.finditer(r'\d+', line)] for line in Input]
Input = [list(line) for line in Input]
symbol_coords = [[xn, yn] for xn in range(0, len(Input[1])) for yn in range(
    0, len(Input)) if not Input[yn][xn].isdigit() and Input[yn][xn] != "."]


part1 = 0
for y, line in enumerate(numbers):
    for x, number in enumerate(line):
        coords = full_number_coords[y][x]
        neighbors = [findNeighbors(xn, yn) for yn, xn in coords]
        neighbors = [coord for number in neighbors for coord in number]

        if any([neighbor in symbol_coords for neighbor in neighbors]):
            part1 = part1 + number


# Part2
gear_coords = [[yn, xn] for xn in range(0, len(Input[1])) for yn in range(0, len(Input)) if Input[yn][xn] == "*"]

part2 = 0
for xg, yg in gear_coords:
    num = []
    neighbors = findNeighbors(xg, yg)
    for y, line in enumerate(numbers):
        for x, number in enumerate(line):
            coords = full_number_coords[y][x]
            if any([coord in neighbors for coord in coords]):
                num.append(number)
    if len(num) == 2:
        part2 = part2 + np.prod(num)

print(part1, part2)
