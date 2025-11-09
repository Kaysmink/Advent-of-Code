import re
from itertools import product
import numpy as np

Input = open("data/2015/dag 15. input.txt", "r").read().split("\n")[0:-1]
ingredients = [list(map(int, re.findall(r"[-\d]+", line))) for line in Input]

poss_cookies = [perm for perm in product(range(101),repeat = len(ingredients)) if sum(perm) == 100]

properties = [[[value*n for value in ingredients[i]] for i, n in enumerate(poss)] for poss in poss_cookies]
property_per_cookie = [[max(sum(comb),0) for comb in zip(*prop)] for prop in properties]

part1 = max([np.prod(comb[0:-1]) for comb in property_per_cookie])
part2 = max([np.prod(comb[0:-1]) for comb in property_per_cookie if comb[-1] == 500])

print(part1, part2)

