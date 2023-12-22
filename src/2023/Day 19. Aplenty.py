import math
from collections import defaultdict
from copy import deepcopy as dc
import regex as re

workflows, parts = open("data/2023/dag 19. input.txt", "r").read().split("\n\n")
workflow_name = [re.findall(r'\w+', line)[0] for line in workflows.split("\n")]
workflows = [re.findall(r'{(\S+)}', line)[0] for line in workflows.split("\n")]
workflows = [line.replace("R", "False").replace("A", "True") for line in workflows]
workflows = [[step.split(":") for step in line.split(",")] for line in workflows]
workflows = {workflow_name[index]: workflow for index, workflow in enumerate(workflows)}

parts = parts.split("\n")[0:-1]
parts = [line[1:-1].replace(",", "\n") for line in parts]


def execute_step(name):
    for rule in workflows[name]:
        if len(rule) == 1:
            return rule[0]
        if eval(rule[0]):
            return rule[1]


def execute_workflows():
    result = "in"
    while result not in ["True", "False"]:
        result = execute_step(result)
    return eval(result)


def add_step(position, constrain):
    constrain = dc(constrain)
    constrain_dict[position].append(constrain)
    if position in ["True", "False"]:
        pass
    else:
        for rule in workflows[position]:
            constrain = dc(constrain)
            if len(rule) == 1:
                add_step(rule[0], constrain)
            else:
                part = rule[0][0]
                minC, maxC = constrain[part]
                const = int(re.findall(r'\d+', rule[0])[0])
                if "<" in rule[0]:
                    constrain[part] = [minC, const - 1]
                    add_step(rule[1], constrain)
                    constrain[part] = [const, maxC]
                if ">" in rule[0]:
                    constrain[part] = [const + 1, maxC]
                    add_step(rule[1], constrain)
                    constrain[part] = [minC, const]

# Part 1
part1 = 0
for part in parts:
    exec(part)
    if execute_workflows():
        numbers = sum(list(map(int, re.findall(r'\d+', part))))
        part1 = part1 + numbers

# Part 2
constrain_dict = defaultdict(list)
add_step("in", {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]})

part2 = 0
for ranges in constrain_dict["True"]:
    part2 = part2 + sum([math.prod([(y - x) + 1 for x, y in ranges.values()])])


print(part1, part2)
