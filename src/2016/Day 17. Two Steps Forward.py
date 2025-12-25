import hashlib

Input = open("data/2016/dag 17. input.txt", "r").read().strip()

step_dict = {"U": [0, -1], "D": [0, 1], "L": [-1, 0], "R": [1, 0]}
door_dict = {0: "U", 1: "D", 2: "L", 3: "R"}

def get_neighbors(x, y, open_doors, path):
    return [(x+xn, y+yn, path+key) for key, (xn,yn) in step_dict.items() if
            0 <= x+xn < 4 and 0 <= y+yn < 4 and key in open_doors]

def walk_through_maze(part, current_positions, end):
    possible_paths = []
    while current_positions:
        new_positions = []
        for x, y, path in current_positions:
            res = hashlib.md5(path.encode()).hexdigest()[0:4]
            open_doors = [door_dict[index] for index, value in enumerate(res) if value in ["b", "c", "d", "e", "f"]]
            pos_positions = get_neighbors(x, y, open_doors, path)
            for x,y,path in pos_positions:
                if (x,y) == end:
                    if part == 1:
                        return path[len(Input):]
                    else:
                        possible_paths.append(path[len(Input):])
                else:
                    new_positions.append((x,y,path))

        current_positions = new_positions
    return possible_paths


start = [(0,0,Input)]
part1 = walk_through_maze(1, start, (3,3))
part2 = max([len(path) for path in walk_through_maze(2, start, (3,3))])

print(part1, part2)