from itertools import combinations
import math

packages = tuple(list(map(int,open("data/2015/dag 24. input.txt", "r").read().split("\n")[0:-1])))

def get_possible_groups(max_size, num_group):
    return [comb for comb in combinations(packages, max_size) if sum(comb) == sum(packages) // num_group]

# The answer was the smallest score of all groups containing 5/6 packages.
# With different inputs this might not be the case.
part1 = min([math.prod(comb) for comb in get_possible_groups(6, 3)])
part2 = min([math.prod(comb) for comb in get_possible_groups(5, 4)])

print(part1, part2)