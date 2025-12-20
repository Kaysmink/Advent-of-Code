from collections import defaultdict

Input = open("data/2016/dag 12. input.txt", "r").read().split("\n")[0:-1]
instructions = [line.split() for line in Input]

def run_program(part):
    registers = defaultdict(int)
    if part == 2:
        registers['c'] = 1

    index = 0
    while True:
        instruction = instructions[index]
        if instruction[0] == "cpy":
            if instruction[1].isnumeric():
                registers[instruction[2]] = int(instruction[1])
            else:
                registers[instruction[2]] = registers[instruction[1]]
        if instruction[0] == "inc":
            registers[instruction[1]] = registers[instruction[1]] + 1
        if instruction[0] == "dec":
            registers[instruction[1]] = registers[instruction[1]]- 1
        if instruction[0] == "jnz":
            if instruction[1].isnumeric():
                if int(instruction[1]) != 0:
                    index += int(instruction[2])
                    continue
            if registers[instruction[1]] != 0:
                index += int(instruction[2])
                continue

        index = index +1
        if index >= len(instructions):
            break

    return registers["a"]

part1 = run_program(1)
part2 = run_program(2)

print(part1, part2)