Input = open("data/2024/dag 20. input.txt", "r").read().split("\n")[0:-1]
Map = [list(line) for line in Input]

current_positions = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "S"]
end = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "E"][0]


def findNeighbors(x, y):
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            0 <= xn < len(Map[0]) and 0 <= yn < len(Map) and (abs(x - xn) + abs(y - yn) == 1)]


def walk_through_maze(Map, current_positions):
    path_dict = {current_positions[0]: 0}

    steps = 0
    while current_positions:
        steps = steps + 1
        new_positions = []
        for x, y in current_positions:
            neighbors = findNeighbors(x, y)
            for xn, yn in neighbors:
                if Map[yn][xn] == "#":
                    continue
                if (xn, yn) not in visited:
                    new_positions.append((xn, yn))
                    visited.add((xn, yn))
                    path_dict[(xn, yn)] = steps
                if (xn, yn) == end:
                    return path_dict

        current_positions = new_positions
    return 0


def get_cheats(sec, threshold):
    result = 0
    for (x, y), value in path_dict.items():
        cheat_ends = [(xn, yn, abs(x - xn) + abs(y - yn)) for xn in range(x - sec, x + sec+1) for yn in range(y - sec, y + sec+1) if
                      0 <= xn < len(Map[0]) and 0 <= yn < len(Map) and (abs(x - xn) + abs(y - yn) <= sec)
                      and (xn, yn) in path_dict.keys() and (xn, yn) != (x, y) and path_dict[(xn, yn)] > path_dict[(x, y)]]

        cheat_ends = [[(x, y), (xn, yn), path_dict[(x, y)] - path_dict[(xn, yn)] + value]
                      for xn, yn, value in cheat_ends if (value + path_dict[(x, y)] - path_dict[(xn, yn)]) != 0]
        result = result + sum([value <= threshold for c1, c2, value in cheat_ends])

    return result


visited = set(current_positions)
path_dict = walk_through_maze(Map, current_positions)

part1 = get_cheats(2, -100)
part2 = get_cheats(20, -100)

print(part1, part2)
