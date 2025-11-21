import re

Input = open("data/2016/dag 03. input.txt", "r").read().split("\n")[0:-1]
sides = [list(map(int,re.findall(r"\d+", line))) for line in Input]

def is_triangle(side):
    return sum(side[0:2]) > side[2]


def parse_input_part2(Input):
    numbers = [list(map(int, re.findall(r"\d+", line))) for line in Input]
    c1,c2,c3 = [[c[i:i + 3] for i in range(0, len(c), 3)] for c in map(list, zip(*numbers))]

    return c1+c2+c3

part1 = sum([is_triangle(sorted(side)) for side in sides])

sides_part2 = parse_input_part2(Input)
part2 = sum([is_triangle(sorted(side)) for side in sides_part2])

print(part1, part2)