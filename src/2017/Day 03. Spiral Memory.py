from collections import defaultdict

Input = int(open("data/2017/dag 03. input.txt", "r").read().strip())

def get_neighbors(x,y):
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            (abs(x - xn) + abs(y - yn) > 0)]

def create_matrix(size):
    locations = [(0, 0)]
    value_dict = defaultdict(int)
    value_dict[(0, 0)] = 1
    part2 = False
    dim = 0

    while len(locations) <= size:
        dim = dim +1
        x,y = locations[-1]
        locations.extend([(x+1,yn) for yn in range(y, -dim-1,-1)])
        x, y = locations[-1]
        locations.extend([(xn, y) for xn in range(x-1, -dim-1, -1)])
        x, y = locations[-1]
        locations.extend([(x, yn) for yn in range(y+1, dim+1)])
        x, y = locations[-1]
        locations.extend([(xn, y) for xn in range(x+1, dim+1)])

    for coord in locations[1:]:
        value = sum([value_dict[neighbor] for neighbor in get_neighbors(*coord)])
        value_dict[coord] = value
        if value > Input and not part2:
            part2 = value

    return sum([abs(value) for value in locations[Input-1]]), part2

part1, part2 = create_matrix(Input)

print(part1, part2)
