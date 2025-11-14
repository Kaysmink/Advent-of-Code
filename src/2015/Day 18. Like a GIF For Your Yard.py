Input = open("data/2015/dag 18. input.txt", "r").read().split("\n")[0:-1]
Map = [list(line) for line in Input]
lights_on = set([(x,y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "#"])


def find_neighbors(x,y):
    neighbors = [(xn,yn) for yn in range(y-1,y+2) for xn in range(x-1,x+2) if 0<=xn<grid and
                                                                              0<=yn<grid and
                                                                              abs(x-xn) + abs(y-yn) > 0]
    return neighbors


def calculate_next_state(x,y, lights_on):
    neighbors = [coord for coord in find_neighbors(x,y) if coord in lights_on]

    if (x,y) in lights_on and len(neighbors) in [2,3]:
        return True
    if (x,y) not in lights_on and len(neighbors) == 3:
        return True
    return False


def run_simulation(part, lights_on, steps):
    if part == 2:
        lights_on.update([(0, 0), (0, grid - 1), (grid - 1, 0), (grid - 1, grid - 1)])

    for step in range(steps):
        lights_on = set([(x,y) for x in range(grid) for y in range(grid) if calculate_next_state(x,y, lights_on)])

        if part == 2:
            lights_on.update([(0, 0), (0, grid - 1), (grid - 1, 0), (grid - 1, grid - 1)])

    return len(lights_on)

grid = 100
part1 = run_simulation(1, lights_on, 100)
part2 = run_simulation(2, lights_on, 100)

print(part1, part2)


