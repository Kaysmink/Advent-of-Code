Input = open("data/2024/dag 18. input.txt", "r").read().split("\n")[0:-1]

current_positions = [(0, 0)]
maxGrid = 71
end = (maxGrid - 1, maxGrid - 1)


def findNeighbors(x, y):
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            0 <= xn < maxGrid and 0 <= yn < maxGrid and (abs(x - xn) + abs(y - yn) == 1) if
            (xn, yn) not in blocks]


def walk_through_maze(current_positions):
    steps = 0
    while current_positions:
        steps = steps + 1
        new_positions = []
        for x, y in current_positions:
            neighbors = findNeighbors(x, y)
            for xn, yn in neighbors:
                if (xn, yn) not in visited:
                    new_positions.append((xn, yn))
                    visited.add((xn, yn))
                if (xn, yn) == end:
                    return steps
        current_positions = new_positions
    return 0


for byteNum in range(1024, len(Input) + 1):
    bytes = [list(map(int, line.split(","))) for index, line in enumerate(Input) if index < byteNum]
    blocks = [(x, y) for x, y in bytes]
    visited = set(current_positions)

    pathLength = walk_through_maze(current_positions)
    if byteNum == 1024:
        part1 = pathLength
    if pathLength == 0:
        part2 = Input[byteNum - 1]
        break

print(part1, part2)
