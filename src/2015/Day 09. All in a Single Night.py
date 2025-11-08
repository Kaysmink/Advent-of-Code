import re
from collections import defaultdict
from itertools import permutations

Input = open("data/2015/dag 09. input.txt", "r").read().split("\n")[0:-1]
routes = [re.findall(r"([a-zA-z]+) to ([a-zA-z]+) = (\d+)", line)[0] for line in Input]

distances = defaultdict(dict)
for start, dest, l in routes:
    distances[start][dest] = int(l)
    distances[dest][start] = int(l)

poss_routes = [perm for perm in permutations(distances.keys(), len(distances.keys()))]
distance = [sum([distances[perm[i]][perm[i+1]] for i in range(len(perm)-1)]) for perm in poss_routes]

part1 = min(distance)
part2 = max(distance)

print(part1, part2)


