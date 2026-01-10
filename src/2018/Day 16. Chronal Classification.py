import re
from collections import defaultdict
from copy import deepcopy

Input = open("data/2018/dag 16. input.txt", "r").read().split("\n\n\n\n")

instructions = [list(map(int,re.findall(r"\d+", line))) for line in Input[0].split("\n\n")]
program = [list(map(int,re.findall(r"\d+", line))) for line in Input[1].split("\n")][0:-1]

def find_possible_opcode(before, instruction, after):
    poss_opcodes = []
    opcode, A, B, C = instruction
    if after[C] == before[A] + before[B]:
        poss_opcodes.append("addr")
    if after[C] == before[A] + B:
        poss_opcodes.append("addi")
    if after[C] == before[A] * before[B]:
        poss_opcodes.append("mulr")
    if after[C] == before[A] * B:
        poss_opcodes.append("muli")
    if after[C] == before[A] & before[B]:
        poss_opcodes.append("banr")
    if after[C] == before[A] & B:
        poss_opcodes.append("bani")
    if after[C] == before[A] | before[B]:
        poss_opcodes.append("borr")
    if after[C] == before[A] | B:
        poss_opcodes.append("bori")
    if after[C] == before[A]:
        poss_opcodes.append("setr")
    if after[C] == A:
        poss_opcodes.append("seti")
    if (after[C] == 1 and A > before[B]) or (after[C] == 0 and A <= before[B]):
        poss_opcodes.append("gtir")
    if (after[C] == 1 and before[A] > B) or (after[C] == 0 and before[A] <= B):
        poss_opcodes.append("gtri")
    if (after[C] == 1 and before[A] > before[B]) or (after[C] == 0 and before[A] <= before[B]):
        poss_opcodes.append("gtrr")
    if (after[C] == 1 and A == before[B]) or (after[C] == 0 and A != before[B]):
        poss_opcodes.append("eqir")
    if (after[C] == 1 and before[A] == B) or (after[C] == 0 and before[A] != B):
        poss_opcodes.append("eqri")
    if (after[C] == 1 and before[A] == before[B]) or (after[C] == 0 and before[A] != before[B]):
        poss_opcodes.append("eqrr")

    return set(poss_opcodes)

def check_opcodes(instruction):
    before, instruction, after = [instruction[i:i + 4] for i in range(0, len(instruction), 4)]
    possible_opcodes = find_possible_opcode(before, instruction, after)
    opcode_dict[instruction[0]].append(possible_opcodes)
    return possible_opcodes

def remove_value(d, r):
    for key, value in d.items():
        d[key] = set([v for v in value if v != r])

    return deepcopy(d)

def set_opcodes(opcode_dict):
    result = defaultdict(str)
    remaining_dict = deepcopy(opcode_dict)
    for key, value in remaining_dict.items():
        remaining_dict[key] = set.intersection(*value)

    while remaining_dict:
        new_remaining = deepcopy(remaining_dict)
        for key, value in remaining_dict.items():
            if len(value) == 1:
                result[key] = list(value)[0]
                del new_remaining[key]
                new_remaining = remove_value(new_remaining, list(value)[0])

        remaining_dict = new_remaining

    return result


def run_program(program):
    registers = defaultdict(int)

    for instruction in program:
        opcode, A, B, C = instruction
        if opcode_dict[opcode] == "addr":
            registers[C] = registers[A] + registers[B]
        if opcode_dict[opcode] == "addi":
            registers[C] = registers[A] + B
        if opcode_dict[opcode] == "mulr":
            registers[C] = registers[A] * registers[B]
        if opcode_dict[opcode] == "muli":
            registers[C] = registers[A] * B
        if opcode_dict[opcode] == "banr":
            registers[C] = registers[A] & registers[B]
        if opcode_dict[opcode] == "bani":
            registers[C] = registers[A] & B
        if opcode_dict[opcode] == "borr":
            registers[C] = registers[A] | registers[B]
        if opcode_dict[opcode] == "bori":
            registers[C] = registers[A] | B
        if opcode_dict[opcode] == "setr":
            registers[C] = registers[A]
        if opcode_dict[opcode] == "seti":
            registers[C] = A
        if opcode_dict[opcode] == "gtir":
            registers[C] = 1 if A > registers[B] else 0
        if opcode_dict[opcode] == "gtri":
            registers[C] = 1 if registers[A] > B else 0
        if opcode_dict[opcode] == "gtrr":
            registers[C] = 1 if registers[A] > registers[B] else 0
        if opcode_dict[opcode] == "eqir":
            registers[C] = 1 if A == registers[B] else 0
        if opcode_dict[opcode] == "eqri":
            registers[C] = 1 if registers[A] == B else 0
        if opcode_dict[opcode] == "eqrr":
            registers[C] = 1 if registers[A] == registers[B] else 0

    return registers[0]

opcode_dict = defaultdict(list)
part1 = sum([len(check_opcodes(instruction)) >= 3 for instruction in instructions])
opcode_dict = set_opcodes(opcode_dict)
part2 = run_program(program)

print(part1, part2)