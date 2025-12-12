import re
from shapely import Polygon

Input = open("data/2025/dag 09. input.txt", "r").read().split("\n")[0:-1]
coords = [tuple(list(map(int,re.findall(r"\d+", line)))) for line in Input]
coord_combinations = set([tuple(sorted([c1,c2])) for c1 in coords for c2 in coords if c1 != c2])


def calculate_area(c1, c2):
    x = abs(c1[0] - c2[0]) +1
    y = abs(c1[1] - c2[1]) +1

    return x*y


def rect_in_polygon(c1,c2):
    coords = [c1,(c1[0],c2[1]), c2, (c2[0],c1[1])]
    pol = Polygon(coords)

    return pol.within(polygon)


polygon = Polygon(coords)
part1 = max([calculate_area(c1,c2) for c1, c2 in coord_combinations])
part2 = max([calculate_area(c1,c2) for c1, c2 in coord_combinations if rect_in_polygon(c1, c2)])

print(part1, part2)
