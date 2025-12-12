import re

Input = open("data/2025/dag 12. input.txt", "r").read().split("\n\n")[-1]
Input = [list(map(int,re.findall(r"\d+", line))) for line in Input.split("\n")[0:-1]]
instructions = [(line[0:2], line[2::]) for line in Input]

part1 = sum([x*y >= sum(values)*7 for [x,y], values in instructions])

print(part1)