from collections import defaultdict
from copy import deepcopy as dc

Input = open("data/2023/dag 17. input.txt", "r").read().split("\n")[0:-1]
Map = [list(map(int, list(line))) for line in Input]

reverse_dict = {0: 3, 1: 2, 2: 1, 3: 0}


def get_neighbors(x, y):
    return [[xn, yn] for xn in range(x-1, x+2) for yn in range(y-1, y+2) if (abs(x-xn) + abs(y-yn) == 1)]


def get_new_positions(current_positions, part):
    global path_dict
    new_positions = []
    for [[x, y], order] in current_positions:
        loss = path_dict[(x, y, tuple(order))]
        neighbors = get_neighbors(x, y)

        for index, [xn, yn] in enumerate(neighbors):
            if part == 1:
                if xn < 0 or yn < 0 or xn >= len(Map[0]) or yn >= len(Map) or reverse_dict[index] == order[-1] or order.count(index) == 3:
                    continue
            if part == 2:
                if xn < 0 or yn < 0 or xn >= len(Map[0]) or yn >= len(Map) or reverse_dict[index] == order[-1] or order.count(index) == 10:
                    continue
                if order[-4::].count(order[-1]) < 4 and index != order[-1]:
                    continue

            value = loss + Map[yn][xn]
            new_order = dc(order)
            new_order.pop(0)
            new_order.append(index)

            if (xn, yn, tuple(new_order)) not in path_dict.keys() or value < path_dict[(xn, yn, tuple(new_order))]:
                path_dict[(xn, yn, tuple(new_order))] = value
                new_positions.append([[xn, yn], new_order])
            else:
                continue
    return new_positions


def shortest_path(current_positions, part):
    while current_positions:
        current_positions = get_new_positions(current_positions, part)


path_dict = defaultdict(int)
shortest_path([[[0, 0], [-1, -1, -1]]], 1)
part1 = min([value for key, value in path_dict.items() if "140, 140" in str(key)])

path_dict = defaultdict(int)
shortest_path([[[0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]], 2)
part2 = min([value for key, value in path_dict.items() if "140, 140" in str(key)])

print(part1, part2)
