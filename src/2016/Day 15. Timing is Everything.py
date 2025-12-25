import re
from collections import deque
from copy import deepcopy

Input = open("data/2016/dag 15. input.txt", "r").read().split("\n")[0:-1]
Input = [list(map(int,re.findall(r"\d+", line))) for line in Input]

def initiate_discs(part, Input):
    discs = {l[0] : deque(range(l[1])) for l in Input}
    [discs[l[0]].rotate(-l[3]) for l in Input]

    if part == 2:
        discs[len(discs)+1] = deque(range(11))
    return discs

def push_button(time, discs):
    discs = deepcopy(discs)
    for num, disc in enumerate(discs.values()):
        disc.rotate(-(time+num+1))
        if disc[0] != 0:
            return False

    return True

def calculate_time(part):
    discs = initiate_discs(part, Input)
    time = 0
    while True:
        if push_button(time, discs):
            return time
        time = time + 1

part1 = calculate_time(1)
part2 = calculate_time(2)

print(part1, part2)