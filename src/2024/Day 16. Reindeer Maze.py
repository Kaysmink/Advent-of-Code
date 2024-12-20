from collections import defaultdict
from copy import deepcopy as dc

Input = open("data/2024/dag 16. input.txt", "r").read().split("\n")[0:-1]
Map = [list(line) for line in Input]
current_positions = [[x, y, ">", 0, [(x, y)]] for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "S"]
end = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "E"][0]

step_dict = {">": [1, 0],
             "<": [-1, 0],
             "^": [0, -1],
             "v": [0, 1]}

rotate_dict = {">": ["v", "^"],
               "<": ["v", "^"],
               "^": ["<", ">"],
               "v": ["<", ">"]}


def next_steps(x, y, direction, value, path):
    next_steps = [(x, y, z, value + 1000, dc(path)) for z in rotate_dict[direction]]

    xn, yn = step_dict[direction]
    x, y = (x + xn, y + yn)
    if Map[y][x] != "#":
        new_path = dc(path)
        new_path.append((x, y))
        next_steps.append((x, y, direction, value + 1, new_path))

    return next_steps


def shortestPath(current_positions):
    global end_value_paths
    while current_positions:
        new_positions = []
        for x, y, direction, value, path in current_positions:
            pos_positions = next_steps(x, y, direction, value, path)
            for xn, yn, directionN, valueN, pathN in pos_positions:
                if (xn, yn, directionN) not in visited.keys() or valueN <= visited[(xn, yn, directionN)]:
                    visited[(xn, yn, directionN)] = valueN
                    if valueN <= end_value_paths:
                        new_positions.append((xn, yn, directionN, valueN, pathN))
                    if (xn, yn) == end:
                        end_paths.append([valueN, pathN])

        current_positions = new_positions


visited = defaultdict(int)
visited[tuple(current_positions[0][0:3])] = 0
end_paths = []
end_value_paths = 65436  # hardcoded value op part1
shortestPath(current_positions)

part1 = min([visited[(end[0], end[1], direction)] for direction in step_dict.keys() if
             visited[(end[0], end[1], direction)] != 0])

shortest_paths = [route for value, route in end_paths if value == part1]
part2 = len(set([value for sub in shortest_paths for value in sub]))

print(part1, part2)
