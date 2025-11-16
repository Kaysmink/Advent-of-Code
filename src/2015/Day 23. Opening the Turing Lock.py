import re

Input = open("data/2015/dag 23. input.txt", "r").read().split("\n")[0:-1]
instructions = [re.findall(r"([a-z]{3}| [a-z]|[\-\d]+)",line) for line in Input]


def run_program(part):
    register = {"a":0, "b":0} if part==1 else {"a":1, "b":0}

    current_instruction = 0
    while current_instruction < len(instructions):
        instruction = instructions[current_instruction]
        instr = instruction[0]

        if instr != "jmp":
            reg = instruction[1].strip()

        register[reg] = (register[reg] / 2 if instr == "hlf" else
                         register[reg] * 3 if instr == "tpl" else
                         register[reg] + 1 if instr == "inc" else
                         register[reg])

        current_instruction = (current_instruction + int(instruction[1]) if instr == "jmp" else
                               current_instruction + int(instruction[2]) if (instr == "jie" and register[reg]%2 == 0) else
                               current_instruction + int(instruction[2]) if (instr == "jio" and register[reg] == 1) else
                               current_instruction +1)

    return register["b"]


part1 = run_program(1)
part2 = run_program(2)

print(part1, part2)


