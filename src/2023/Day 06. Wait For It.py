import regex as re
import numpy as np


Input = open("data/2023/dag 06. input.txt", "r").read().split("\n")[0:-1]
Input = [list(map(int, re.findall(r'\d+', line))) for line in Input]

time = int("".join(list(map(str, Input[0]))))
winning = int("".join(list(map(str, Input[1]))))

part1 = np.prod([len([sec * (Input[0][index] - sec) for sec in range(0, Input[0][index])
                      if sec * (Input[0][index] - sec) > Input[1][index]])
                 for index, value in enumerate(Input[0])])

part2 = len([sec * (time - sec) for sec in range(0, time) if sec * (time - sec) > winning])

print(part1, part2)
