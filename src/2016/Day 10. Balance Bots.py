import math
import re
from collections import defaultdict

Input = open("data/2016/dag 10. input.txt", "r").read().split("\n")[0:-1]
instructions = [re.findall(r"bot|value|\d+|output", line) for line in Input]

bots = defaultdict(list)
while instructions:
    for index, instr in enumerate(instructions):
        if instr[0] == "bot":
            b,fr,bl,toL,bh,toH = instr
            if len(bots[b+fr]) != 2:
                continue
            else:
                low, high = sorted(bots[b+fr])
                bots[b+fr] = (low,high)
                bots[bl+toL].append(low)
                bots[bh+toH].append(high)

        if instr[0] == "value":
            v,value,b,to = instr
            bots[b+to].append(int(value))
        instructions.pop(index)

part1 = [key for key, value in bots.items() if value == (17,61)][0][3::]
part2 = math.prod([value[0] for key, value in bots.items() if key in ["output0","output1","output2"]])

print(part1, part2)

