from itertools import accumulate

Input = open("data/2015/dag 01. input.txt", "r").read()

part1 = sum([1 if value == "(" else -1 for value in Input])
part2 = list(accumulate([1 if value == "(" else -1 for value in Input])).index(-1)+1

print(part1, part2)