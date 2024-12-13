from collections import deque, defaultdict

Input = open("data/2024/dag 12. input.txt", "r").read().split("\n")[0:-1]
# Input = open("data/2024/test.txt", "r").read().split("\n")[0:-1]
Map = [list(line) for line in Input]


def findNeighbors(x, y, plant):
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            0 <= xn < len(Input[0]) and 0 <= yn < len(Input) and (abs(x - xn) + abs(y - yn) == 1) and Input[yn][
                xn] == plant]


def find_area(Input, x, y):
    area = [(x, y)]

    q = deque()
    q.append((x, y))

    plant = Input[y][x]

    while q:
        x, y = q.popleft()
        neighbors = findNeighbors(x, y, plant)
        for x, y in neighbors:
            if (x, y) in area:
                continue
            area.append((x, y))
            q.append((x, y))

    return area


def parse_input(Input):
    checked = set()
    gardens = defaultdict(list)
    for x in range(len(Input[0])):
        for y in range(len(Input)):
            if (x, y) in checked:
                continue
            area = find_area(Input, x, y)

            plant = Input[y][x]
            checked.update(area)
            gardens[plant].append(area)
    return gardens


def calculate_perimeter(garden):
    perimeter = 0
    for x, y in garden:
        neighbors = [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
                     (abs(x - xn) + abs(y - yn) == 1)]
        perimeter = perimeter + sum([neighbor not in garden for neighbor in neighbors])
    return perimeter


Map = parse_input(Input)
gardens = [garden for sub in Map.values() for garden in sub]
part1 = sum([len(garden) * calculate_perimeter(garden) for garden in gardens])


def is_corner(garden, x, y):
    neighbors = [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
                 (abs(x - xn) + abs(y - yn) == 1)]
    valid_neighbor = [neighbor in garden for neighbor in neighbors]
    pass


print(part1)
