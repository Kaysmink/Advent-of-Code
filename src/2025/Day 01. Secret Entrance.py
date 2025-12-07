from collections import deque

Input = open("data/2025/dag 01. input.txt", "r").read()
instructions = list(map(int,Input.replace("L", "-").replace("R", "").split("\n")[0:-1]))

clicks = [0,0]
clock = deque(range(0,100))
clock.rotate(-50)
for instruction in instructions:
    full_rotations, remainder = divmod(abs(instruction), 100)
    if instruction > 0:
        extra_click = 1 if clock[0] + remainder > 99 and clock[0] != 0  else 0
    else:
        extra_click = 1 if clock[0] - remainder <= 0 and clock[0] != 0 else 0

    clicks[1] = clicks[1] + full_rotations + extra_click

    clock.rotate(-instruction)
    if clock[0] == 0:
        clicks[0] = clicks[0] + 1

part1, part2 = clicks

print(part1, part2)