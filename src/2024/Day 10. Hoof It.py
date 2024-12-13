Input = open("data/2024/dag 10. input.txt", "r").read().split("\n")[0:-1]
Map = [list(map(int, list(line))) for line in Input]

startPos = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == 0]


def findNeighbors(x, y):
    height = Map[y][x]
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            0 <= xn < len(Input[0]) and 0 <= yn < len(Input) and (abs(x - xn) + abs(y - yn) == 1) and Map[yn][xn] == (
                    height + 1)]


def walk_through_map(current_positions):
    visited_tops = []
    while current_positions:
        new_positions = [findNeighbors(x, y) for x, y in current_positions]
        tops = [(x, y) for sub in new_positions for (x, y) in sub if Map[y][x] == 9]
        current_positions = [(x, y) for sub in new_positions for (x, y) in sub if Map[y][x] != 9]
        visited_tops.extend(tops)

    return visited_tops


visited_tops = [walk_through_map([pos]) for pos in startPos]
part1 = sum([len(set(top)) for top in visited_tops])
part2 = len([value for sub in visited_tops for value in sub])

print(part1, part2)
