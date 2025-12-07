import math
import re

Input = open("data/2025/dag 06. input.txt", "r").read().split("\n")[0:-1]
values = [re.findall(r"\d+|\+|\*", line) for line in Input]
problems = list(zip(*values))

def calculate(problem, operator=False):
    if not operator:
        operator = problem[-1]
        problem = problem[:-1]

    if operator == "+":
        return sum(list(map(int, problem)))
    if operator == "*":
        return math.prod(list(map(int, problem)))

def calculate_part2():
    Input = open("data/2025/dag 06. input.txt", "r").read().split("\n")[0:-1]
    operators = re.findall(r"\+|\*", Input[-1])
    values = [re.findall(r"\d| ", line) for line in Input[0:-1]]

    problems = [problem if problem != (' ', ' ', ' ', ' ') else list("SPLIT") for problem in list(zip(*values))]
    problems = " ".join(["".join(value) for value in problems]).split("SPLIT")
    problems = [re.findall(r"\d+", problem) for problem in problems]

    part2 = sum(calculate(problem, operators[i]) for i, problem in enumerate(problems))

    return part2

part1 = sum([calculate(problem) for problem in problems])
part2 = calculate_part2()

print(part1, part2)