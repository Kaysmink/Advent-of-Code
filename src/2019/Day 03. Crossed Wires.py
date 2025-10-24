Input = open("data/2019/dag 03. input.txt", "r").read().split("\n")[0:-1]
wires = [line.split(",") for line in Input]

step_dict = {"R": [1, 0],
             "L": [-1, 0],
             "U": [0, -1],
             "D": [0, 1]}


def new_coords(curentPos, dir, value):
    x,y = curentPos
    xn, yn = step_dict[dir]
    new_coords = [(x + xn*step, y + yn*step) for step in range(1,value+1)]

    return new_coords


def create_wires(wire):
    coords = [(0,0)]

    for step in wire:
        dir, value = [step[0], int(step[1::])]
        coords.extend(new_coords(coords[-1], dir, value))

    return coords[1::]

fences = [create_wires(wire) for wire in wires]
intersections = set(fences[0]).intersection(set(fences[1]))

part1 = min([abs(0-x) + abs(0-y) for x,y in intersections])
part2 = min([fences[0].index(intersection) + fences[1].index(intersection) +2 for intersection in intersections])

print(part1, part2)
