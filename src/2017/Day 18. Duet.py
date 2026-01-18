from collections import defaultdict

instructions = open("data/2017/dag 18. input.txt", "r").read().split("\n")[0:-1]

def run_progam(instructions):
    registers = defaultdict(int)
    index = 0
    while 0<=index<len(instructions):
        instruction = instructions[index]
        if instruction.startswith("snd"):
            instr, value = instruction.split(" ")
            last_frequency = int(value) if value.lstrip('-').isdigit() else registers[value]
        if instruction.startswith("set"):
            instr, reg, value = instruction.split(" ")
            registers[reg] = int(value) if value.lstrip('-').isdigit() else registers[value]
        if instruction.startswith("add"):
            instr, reg, value = instruction.split(" ")
            registers[reg] += int(value) if value.lstrip('-').isdigit() else registers[value]
        if instruction.startswith("mul"):
            instr, reg, value = instruction.split(" ")
            registers[reg] *= int(value) if value.lstrip('-').isdigit() else registers[value]
        if instruction.startswith("mod"):
            instr, reg, value = instruction.split(" ")
            registers[reg] %= int(value) if value.lstrip('-').isdigit() else registers[value]
        if instruction.startswith("rcv"):
            instr, value = instruction.split(" ")
            value = int(value) if value.lstrip('-').isdigit() else registers[value]
            if value != 0:
                return last_frequency
        if instruction.startswith("jgz"):
            instr, value, jump = instruction.split(" ")
            value = int(value) if value.lstrip('-').isdigit() else registers[value]
            jump = int(jump) if jump.lstrip('-').isdigit() else registers[jump]
            if value > 0:
                index = index + jump
                continue

        index = index + 1

def run_multi_programs(instructions):
    registers = [defaultdict(int), defaultdict(int)]
    registers[0]["p"] = 0
    registers[1]["p"] = 1
    indexes = [0, 0]
    sending = [[], []]
    waiting = [False, False]
    terminated = [False, False]
    values_send = [0,0]
    while sum(terminated) != 2 and sum(waiting) != 2:
        running_programs = [i for i, value in enumerate(terminated) if not value]
        for index_p in running_programs:
            instruction = instructions[indexes[index_p]]
            if instruction.startswith("snd"):
                instr, value = instruction.split(" ")
                value = int(value) if value.lstrip('-').isdigit() else registers[index_p][value]
                sending[index_p].append(value)
                values_send[index_p] += 1
            if instruction.startswith("set"):
                instr, reg, value = instruction.split(" ")
                registers[index_p][reg] = int(value) if value.lstrip('-').isdigit() else registers[index_p][value]
            if instruction.startswith("add"):
                instr, reg, value = instruction.split(" ")
                registers[index_p][reg] += int(value) if value.lstrip('-').isdigit() else registers[index_p][value]
            if instruction.startswith("mul"):
                instr, reg, value = instruction.split(" ")
                registers[index_p][reg] *= int(value) if value.lstrip('-').isdigit() else registers[index_p][value]
            if instruction.startswith("mod"):
                instr, reg, value = instruction.split(" ")
                registers[index_p][reg] %= int(value) if value.lstrip('-').isdigit() else registers[index_p][value]
            if instruction.startswith("rcv"):
                instr, reg = instruction.split(" ")
                index_s = 0 if index_p == 1 else 1
                if sending[index_s]:
                    registers[index_p][reg] = sending[index_s].pop(0)
                else:
                    waiting[index_p] = True
                    continue
            if instruction.startswith("jgz"):
                instr, value, jump = instruction.split(" ")
                value = int(value) if value.lstrip('-').isdigit() else registers[index_p][value]
                jump = int(jump) if jump.lstrip('-').isdigit() else registers[index_p][jump]
                if value > 0:
                    indexes[index_p] = indexes[index_p] + jump
                    if not 0<=indexes[index_p]<len(instructions):
                        terminated[index_p] = True
                    continue

            indexes[index_p] = indexes[index_p] + 1
            if not 0 <= indexes[index_p] < len(instructions):
                terminated[index_p] = True

    return values_send[1]

part1 = run_progam(instructions)
part2 = run_multi_programs(instructions)

print(part1, part2)