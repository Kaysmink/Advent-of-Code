from collections import defaultdict

Input = open("data/2017/dag 08. input.txt", "r").read().split("\n")[0:-1]
instructions = [line.split(" if ") for line in Input]

def run_program(instructions):
    registers = defaultdict(int)
    part2 = 0

    for instruction, condition in instructions:
        x = registers[condition.split(" ")[0]]
        condition = "x " + " ".join(condition.split(" ")[1:])

        if eval(condition):
            reg, instr, value = instruction.split()
            if instr == "inc":
                registers[reg] += int(value)
            if instr == "dec":
                registers[reg] -= int(value)

        part2 = max(part2, max(registers.values()))

    return max(registers.values()), part2

part1, part2 = run_program(instructions)

print(part1, part2)