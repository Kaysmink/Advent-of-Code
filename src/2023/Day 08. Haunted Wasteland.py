import numpy as np
import regex as re
from collections import deque

Input = open("data/2023/dag 08. input.txt", "r").read().split("\n\n")

instructions = [0 if char == "L" else 1 for char in Input[0]]
instructions = deque(instructions)
nodes = [re.findall(r'[0-9A-Z]{3}', line) for line in Input[1].split("\n")[0:-1]]
node_dict = {node[0]: [node[1], node[2]] for node in nodes}


def new_node(current, direction):
    return node_dict[current][direction]


def follow_instructions(current_node, part):
    steps = 0
    if part == 1:
        while current_node != "ZZZ":
            current_node = new_node(current_node, instructions[0])
            instructions.rotate(-1)
            steps = steps + 1
        return steps
    if part == 2:
        while not current_node.endswith("Z"):
            current_node = new_node(current_node, instructions[0])
            instructions.rotate(-1)
            steps = steps + 1
        return steps


part1 = follow_instructions("AAA", 1)


# Part2
current_nodes = [node for node in node_dict.keys() if node.endswith("A")]
steps = [follow_instructions(node, 2) for node in current_nodes]

part2 = np.lcm.reduce(steps, dtype=np.int64)

print(part1, part2)
