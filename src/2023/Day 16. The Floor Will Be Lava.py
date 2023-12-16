from collections import defaultdict

Input = open("data/2023/dag 16. input.txt", "r").read().split("\n")[0:-1]
cave = [list(line) for line in Input]


step_dict = {"\\": {"S": [[1, 0]], "N": [[-1, 0]], "E": [[0, 1]], "W": [[0, -1]]},
             "/": {"S": [[-1, 0]], "N": [[1, 0]], "E": [[0, -1]], "W": [[0, 1]]},
             ".": {"S": [[0, 1]], "N": [[0, -1]], "E": [[1, 0]], "W": [[-1, 0]]},
             "-": {"S": [[-1, 0], [1, 0]], "N": [[-1, 0], [1, 0]], "E": [[1, 0]], "W": [[-1, 0]]},
             "|": {"S": [[0, 1]], "N": [[0, -1]], "E": [[0, 1], [0, -1]], "W": [[0, 1], [0, -1]]}}

direction_dict = {"|": {"S": "S", "N": "N", "E": "SN", "W": "SN"},
                  "-": {"S": "WE", "N": "WE", "E": "E", "W": "W"},
                  "\\": {"S": "E", "N": "W", "E": "S", "W": "N"},
                  ".": {"S": "S", "N": "N", "E": "E", "W": "W"},
                  "/": {"S": "W", "N": "E", "E": "N", "W": "S"}}


def new_position(poss):
    x, y, direction, symbol = poss
    next_position = [[x+xn, y+yn] for xn, yn in step_dict[symbol][direction]]
    next_direction = list(direction_dict[symbol][direction])

    new_positions = [(xn, yn, next_direction[i], cave[yn][xn]) for i, [xn, yn] in enumerate(
        next_position) if xn >= 0 and xn < len(cave[0]) and yn >= 0 and yn < len(cave)]
    new_positions = [poss for poss in new_positions if poss not in visited.keys()]

    return new_positions


def move_lightbeams(current_positions):
    new_positions = []
    for poss in current_positions:
        new_poss = new_position(poss)
        if new_poss:
            new_positions.extend(new_poss)

    for poss in new_positions:
        visited[poss] = True
    return new_positions


def energized_tiles(current_positions):
    global visited
    visited[list(current_positions)[0]] = True

    while current_positions:
        current_positions = move_lightbeams(current_positions)


def get_start_position(x, y):
    if x == 0:
        direction = "E"
    if x == len(cave) - 1:
        direction = "W"
    if y == 0:
        direction = "S"
    if y == len(cave) - 1:
        direction = "N"

    return {(x, y, direction, cave[y][x])}


# Part 1
current_positions = {(0, 0, "E", "\\")}
visited = defaultdict(bool)
energized_tiles(current_positions)
part1 = len(set([(x, y) for x, y, d, s in visited.keys()]))

# Part 2
start_positions = [get_start_position(x, y) for x in range(0, len(cave[0]))
                   for y in range(0, len(cave)) if x in [0, len(cave[0])-1] or y in [0, len(cave)-1]]

results = []
for index, start_pos in enumerate(start_positions):
    visited = defaultdict(bool)
    energized_tiles(start_pos)
    results.append(len(set([(x, y) for x, y, d, s in visited.keys()])))

part2 = max(results)

print(part1, part2)
