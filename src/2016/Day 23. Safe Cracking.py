import math
from collections import defaultdict
from copy import deepcopy

Input = open("data/2016/dag 23. input.txt", "r").read().split("\n")[0:-1]
instructions = [line.split() for line in Input]


def change_instruction(instruction):
    new_instruction = deepcopy(instruction)
    if len(new_instruction) == 2:
        new_instruction[0] = "dec" if new_instruction[0] == "inc" else "inc"
    if len(new_instruction) == 3:
        new_instruction[0] = "cpy" if new_instruction[0] == "jnz" else "jnz"
    return new_instruction


def check_valid_instruction(instruction):
    if instruction[0] == "cpy":
        if instruction[2].isnumeric():
            return False
    if instruction[0] in ["inc", "dec"]:
        if instruction[1].isnumeric():
            return False
    return True

def run_program(a, instructions):
    instructions = deepcopy(instructions)
    registers = defaultdict(int)
    registers['a'] = a

    index = 0
    while index < len(instructions):
        instruction = instructions[index]
        #print(index, len(instructions))
        if not check_valid_instruction(instruction):
            index = index +1
            if index >= len(instructions):
                break
            continue
        if instruction[0] == "cpy":
            if instruction[1].lstrip('-').isdigit():
                registers[instruction[2]] = int(instruction[1])
            else:
                registers[instruction[2]] = registers[instruction[1]]
        if instruction[0] == "inc":
            registers[instruction[1]] = registers[instruction[1]] + 1
        if instruction[0] == "dec":
            registers[instruction[1]] = registers[instruction[1]]- 1
        if instruction[0] == "jnz":
            value = int(instruction[1]) if instruction[1].isnumeric() else registers[instruction[1]]
            if value != 0:
                steps = int(instruction[2]) if instruction[2].lstrip('-').isdigit() else registers[instruction[2]]
                index += steps
                if steps == 0:
                    index = index +1
                continue
        if instruction[0] == "tgl":
            toggle_index = index + registers[instruction[1]]
            if toggle_index >= len(instructions):
                index = index + 1
                continue
            instructions[toggle_index] = change_instruction(instructions[toggle_index])

        index = index +1

    return registers["a"]


part1 = run_program(7, instructions)
part2 = math.factorial(12) + 71*72

print(part1, part2)