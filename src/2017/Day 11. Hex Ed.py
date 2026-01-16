steps = open("data/2017/dag 11. input.txt", "r").read().strip().split(",")

step_dict = {"n":(0,-1,1),
             "ne":(1,-1,0),
             "se":(1,0,-1),
             "s":(0,1,-1),
             "sw":(-1,1,0),
             "nw":(-1,0,1)}

def walk_grid(steps):
    part2 = 0

    pos = [0,0,0]
    for step in steps:
        pos = [sum(p) for p in zip(pos, step_dict[step])]
        part2 = max(part2, max([abs(p) for p in pos]))

    return max([abs(p) for p in pos]), part2

part1, part2 = walk_grid(steps)

print(part1, part2)