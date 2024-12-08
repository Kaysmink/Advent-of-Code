from collections import defaultdict
import itertools as it

Input = open("data/2024/dag 08. input.txt", "r").read().split("\n")[0:-1]
Input = [list(line) for line in Input]

antennaDict = defaultdict(list)

create_dict = [antennaDict[Input[y][x]].append((x, y)) for x in range(
    len(Input[0])) for y in range(len(Input)) if Input[y][x] != "."]


def get_antinodes(antennas, part=1):
    antinodes = []
    for comb in it.combinations(antennas, 2):
        c1, c2 = sorted(comb)
        x1, x2, y1, y2 = c1[0], c2[0], c1[1], c2[1]

        slope = (y1-y2)/(x1-x2)
        start = (x1*y2 - x2*y1)/(x1-x2)

        xn = [[x1-(x2-x1)*n, x2+(x2-x1)*n] for n in range(1, len(Input[0]) // (x2-x1) + 1)]
        xn = xn[0] if part == 1 else [value for sub in xn for value in sub if value >= 0 and value < len(Input[0])]

        new_antinodes = [(x, round(slope*x + start)) for x in xn]
        new_antinodes = [(x, y) for x, y in new_antinodes if x >=
                         0 and x < len(Input[0]) and y >= 0 and y < len(Input)]

        antinodes.extend(new_antinodes)
        if part == 2:
            antinodes.extend([(x1, y1), (x2, y2)])
    return antinodes


antinodes1, antinodes2 = [[get_antinodes(coords, part) for antenna, coords in antennaDict.items()] for part in [1, 2]]

part1 = len(set([value for sub in antinodes1 for value in sub]))
part2 = len(set([value for sub in antinodes2 for value in sub]))

print(part1, part2)
