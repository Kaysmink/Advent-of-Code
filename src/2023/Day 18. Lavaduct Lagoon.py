from shapely import Polygon

Input = open("data/2023/dag 18. input.txt", "r").read().split("\n")[0:-1]
instructions = [line.split(" ") for line in Input]

step_dict = {"R": [1, 0],
             "L": [-1, 0],
             "U": [0, 1],
             "D": [0, -1]}

def get_hex_value(hexa):
    steps = int(hexa[2:-2], 16)
    dir = "R" if hexa[-2] == "0" else "D" if hexa[-2] == "1" else "L" if hexa[-2] == "2" else "U"

    return dir, steps

def get_area(part, instructions):
    coords = [(0,0)]
    current_coord = (0,0)
    for dir, steps, hexa in instructions:
        if part == 2:
            dir, steps = get_hex_value(hexa)

        xn,yn = step_dict[dir]
        current_coord = (current_coord[0] + xn*int(steps), current_coord[1] + yn*int(steps))
        coords.append(current_coord)

    polygon = Polygon(coords)

    return int(polygon.area + polygon.length/2+1)

part1 = get_area(1, instructions)
part2 = get_area(2, instructions)

print(part1, part2)