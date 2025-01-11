import re

Input = open("data/2024/dag 17. input.txt", "r").read().split("\n\n")
Input = [re.findall(r'\d+', line) for line in Input]
registers = {reg: int(value) for reg, value in zip(["A", "B", "C"], Input[0])}
program = [int(value) for value in Input[1]]


def combo(operand):
    if operand in [0, 1, 2, 3]:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]


def run_program(program):
    output = []
    pointer = 0
    while True:
        opcode, operand = program[pointer:pointer + 2]
        if opcode == 0:
            registers["A"] = int(registers["A"] / (2 ** combo(operand)))
        if opcode == 1:
            registers["B"] = registers["B"] ^ operand
        if opcode == 2:
            registers["B"] = combo(operand) % 8
        if opcode == 3:
            pointer = pointer + 2 if registers["A"] == 0 else operand
        if opcode == 4:
            registers["B"] = registers["B"] ^ registers["C"]
        if opcode == 5:
            output.append(combo(operand) % 8)
        if opcode == 6:
            registers["B"] = int(registers["A"] / (2 ** combo(operand)))
        if opcode == 7:
            registers["C"] = int(registers["A"] / (2 ** combo(operand)))
        if opcode != 3:
            pointer = pointer + 2
        if pointer >= len(program) - 1:
            return output


result = run_program(program)
part1 = ",".join(list(map(str, result)))

# for A > 8**X there will be x+1 values in output
# therefore minimum A for 16 values == 8**15
# for every increment of 8**X where X <15 the x+1th value will change.
# therefore incrementing A with 8**X while decreasing X if you find the X+1st value will give te lowest A possible
part2 = 8 ** 15
inc_num = 14
result = []
while result != program:
    part2 = part2 + (8 ** inc_num)
    registers = {"A": part2, "B": 0, "C": 0}
    result = run_program(program)
    if result[-(len(program) - inc_num):] == program[-(len(program) - inc_num):]:
        inc_num = inc_num - 1
        continue

print(part1, part2)
