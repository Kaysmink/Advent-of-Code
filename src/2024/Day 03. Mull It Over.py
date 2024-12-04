import re

Input = open("data/2024/dag 03. input.txt", "r").read()

# Part 1
multi = re.findall(r'mul\(\d+,\d+\)', Input)
numbers = [list(map(int, re.findall(r'\d+', line))) for line in multi]
part1 = sum([num1 * num2 for num1, num2 in numbers])

# part2
multi = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", Input)
instruction = "do()"

part2 = 0
for line in multi:
    if "do" in line:
        instruction = line
        continue
    if instruction == "do()":
        num1, num2 = list(map(int, re.findall(r'\d+', line)))
        part2 = part2 + (num1 * num2)

print(part1, part2)
