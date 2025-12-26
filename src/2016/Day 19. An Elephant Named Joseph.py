from collections import deque
from copy import deepcopy

Input = int(open("data/2016/dag 19. input.txt", "r").read().strip())
elves = deque([(elf,1) for elf in range(1,Input+1)])

def steal_presents(elves, part):
    elves = deepcopy(elves)
    while len(elves) > 1:
        if part == 1:
            elves.rotate(-1)
            eL, pL = elves.popleft()
            e, p = elves[-1]
            elves[-1] = (e,p+pL)
        if part == 2:
            middle = len(elves)//2
            elves.rotate(-middle)
            eL, pL = elves.popleft()
            elves.rotate(middle)
            e, p = elves[0]
            elves[0] = (e, p + pL)
            elves.rotate(-1)

    return elves.popleft()[0]

part1 = steal_presents(elves, 1)
part2 = steal_presents(elves, 2)

print(part1, part2)