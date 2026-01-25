import re
from collections import defaultdict

Input = open("data/2017/dag 25. input.txt", "r").read().split("\n\n")
state, steps = re.findall(r"[A-Z]{1}[.:]|\d+", Input[0])
instructions = [re.findall(r"[A-Z]{1}[.:]|\d+|left|right", line) for line in Input[1:]]

def create_instruction_dict(instructions):
    instruction_dict = defaultdict(dict)
    for s,v1,w1,m1,ns1,v2,w2,m2,ns2 in instructions:
        instruction_dict[s[0:-1]][int(v1)] = {"write": int(w1), "move": m1, "next_state": ns1[0:-1]}
        instruction_dict[s[0:-1]][int(v2)] = {"write": int(w2), "move": m2, "next_state": ns2[0:-1]}
    return instruction_dict

def run_program(state, steps):
    pos = 0
    slots = defaultdict(int)

    for step in range(steps):
        cur_value = slots[pos]
        slots[pos] = instruction_dict[state][cur_value]["write"]
        pos = pos + 1 if instruction_dict[state][cur_value]["move"] == "right" else pos - 1
        state = instruction_dict[state][cur_value]["next_state"]

    return sum(slots.values())

instruction_dict = create_instruction_dict(instructions)
part1 = run_program(state[0:-1], int(steps))

print(part1)