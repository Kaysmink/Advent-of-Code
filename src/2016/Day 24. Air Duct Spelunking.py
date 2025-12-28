from itertools import permutations

Input = open("data/2016/dag 24. input.txt", "r").read().split("\n")[0:-1]
maze = {(x,y) for y in range(len(Input)) for x in range(len(Input[y])) if Input[y][x] != "#"}

def get_neighbors(x, y):
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            (xn,yn) in maze and (abs(x - xn) + abs(y - yn) == 1)]

def find_shortest_path(current_positions, end):
    visited = set()
    steps = 0
    while current_positions:
        steps += 1
        new_positions = []
        for pos in current_positions:
            for neighbor in get_neighbors(*pos):
                if neighbor not in visited:
                    new_positions.append(neighbor)
                    visited.add(neighbor)
                if neighbor == end:
                    return steps
        current_positions = new_positions

def get_route_distance(part):
    distances = []
    for route in permutations("1234567", 7):
        route = ["0"]+list(route) if part == 1 else ["0"] + list(route) + ["0"]
        dist = sum([dist_dict[route[i-1]][route[i]] for i in range(1, len(route))])
        distances.append(dist)
    return min(distances)


goals = {Input[y][x]: (x,y) for y in range(len(Input)) for x in range(len(Input[y])) if Input[y][x] in ["0","1","2","3","4","5","6","7"]}
dist_dict = {g1:{g2:find_shortest_path([c1], c2) for g2,c2 in goals.items() if g1!=g2} for g1, c1 in goals.items()}

part1 = get_route_distance(1)
part2 = get_route_distance(2)

print(part1, part2)