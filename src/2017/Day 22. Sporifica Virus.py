Input = open("data/2017/dag 22. input.txt", "r").read().split("\n")[0:-1]

step_dict = {">": [1, 0],
             "<": [-1, 0],
             "^": [0, -1],
             "v": [0, 1]}

rotate_dict = {">": {".": "^", "#": "v", "W": ">", "F": "<"},
               "<": {".": "v", "#": "^", "W": "<", "F": ">"},
               "^": {".": "<", "#": ">", "W": "^", "F": "v"},
               "v": {".": ">", "#": "<", "W": "v", "F": "^"}}


def walk_carrier(steps, part):
    node_states = {(x, y): Input[y][x] for x in range(len(Input[0])) for y in range(len(Input)) if Input[y][x] == "#"}
    x, y, dir = 12, 12, "^"

    infected = 0
    for step in range(steps):
        if (x,y) not in node_states:
            node_states[(x,y)] = "."

        state = node_states[(x,y)]
        dir = rotate_dict[dir][state]

        if state == "#":
            node_states[(x,y)] = "." if part == 1 else "F"
        if state == ".":
            node_states[(x,y)] = "#" if part == 1 else "W"
            if part == 1:
                infected = infected + 1
        if state == "W":
            node_states[(x,y)] = "#"
            infected = infected + 1
        if state == "F":
            node_states[(x, y)] = "."

        xn,yn = step_dict[dir]
        x,y = x+xn, y+yn

    return infected

part1 = walk_carrier(10000, 1)
part2 = walk_carrier(10000000, 2)

print(part1, part2)