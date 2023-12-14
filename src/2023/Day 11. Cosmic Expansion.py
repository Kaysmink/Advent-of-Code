Input = open("data/2023/dag 11. input.txt", "r").read().split("\n")[0:-1]
universe = [list(line) for line in Input]


def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return abs(x1 - x2) + abs(y1 - y2)


def expand_galaxies(galaxies, expand_num):
    emptyRows = [index for index, row in enumerate(universe) if "#" not in row]
    columns = [[row[i] for row in universe] for i in range(0, len(universe[0]))]
    emptyColumns = [index for index, col in enumerate(columns) if "#" not in col]

    new_galaxies = []
    for x, y in galaxies:
        add_rows = sum(rowNum < y for rowNum in emptyRows)
        add_cols = sum(colNum < x for colNum in emptyColumns)
        new_galaxies.append([x + (add_cols * expand_num), y + (add_rows * expand_num)])

    return new_galaxies


def get_total_distances(galaxies):
    result = 0
    for galaxy in galaxies:
        result = result + sum([distance(galaxy, coord) for coord in galaxies])

    return result // 2


galaxies = [[xn, yn] for xn in range(0, len(universe[1])) for yn in range(0, len(universe)) if universe[yn][xn] == "#"]

# part 1
galaxies_part1 = expand_galaxies(galaxies, 1)
part1 = get_total_distances(galaxies_part1)

# part 2
galaxies_part2 = expand_galaxies(galaxies, 999999)
part2 = get_total_distances(galaxies_part2)

print(part1, part2)
