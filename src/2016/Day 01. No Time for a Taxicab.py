import re

steps = [re.findall(r"[LR]|\d+", line) for line in open("data/2016/dag 01. input.txt", "r").read().strip().split(",")]

step_dict = {">": [1, 0],
             "<": [-1, 0],
             "^": [0, -1],
             "v": [0, 1]}

new_direction = {">": {"R": "v", "L": "^"},
                 "<": {"R": "^", "L": "v"},
                 "^": {"R": ">", "L": "<"},
                 "v": {"R": "<", "L": ">"}}

def walk():
    x = y = part2 = 0
    visited = []
    direction = "^"
    for turn, n in steps:
        direction = new_direction[direction][turn]
        xn, yn = step_dict[direction]
        for step in range(int(n)):
            x, y = (x + xn, y + yn)
            if (x,y) in visited and part2 == 0:
                part2 = abs(x)+abs(y)
            visited.append((x, y))

    return (x,y, part2)


x,y, part2 = walk()
part1 = abs(x)+abs(y)

print(part1, part2)