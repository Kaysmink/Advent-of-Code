from collections import defaultdict
from copy import deepcopy

Input = open("data/2016/dag 25. input.txt", "r").read().split("\n")[0:-1]
instructions = [line.split() for line in Input]


def run_program(a, instructions):
    instructions = deepcopy(instructions)
    registers = defaultdict(int)
    registers['a'] = a

    index = 0
    output_num = 0
    output = "start"
    while index < len(instructions) and output_num < 10000:
        instruction = instructions[index]
        if instruction[0] == "cpy":
            if instruction[1].lstrip('-').isdigit():
                registers[instruction[2]] = int(instruction[1])
            else:
                registers[instruction[2]] = registers[instruction[1]]
        if instruction[0] == "inc":
            registers[instruction[1]] = registers[instruction[1]] + 1
        if instruction[0] == "dec":
            registers[instruction[1]] = registers[instruction[1]] - 1
        if instruction[0] == "jnz":
            value = int(instruction[1]) if instruction[1].isnumeric() else registers[instruction[1]]
            if value != 0:
                steps = int(instruction[2]) if instruction[2].lstrip('-').isdigit() else registers[instruction[2]]
                index += steps
                if steps == 0:
                    index = index + 1
                continue
        if instruction[0] == "out":
            new_output = int(instruction[1]) if instruction[1].lstrip('-').isdigit() else registers[instruction[1]]
            if new_output not in [0,1] or new_output == output:
                return False
            else:
                output = new_output
                output_num = output_num + 1
        index = index + 1

    return True

a=0
while True:
    if run_program(a, instructions):
        part1 = a
        break
    a = a +1

print(part1)
