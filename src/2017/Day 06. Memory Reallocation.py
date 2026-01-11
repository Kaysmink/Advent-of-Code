import re
from collections import defaultdict

banks = list(map(int,re.findall(r"\d+",open("data/2017/dag 06. input.txt", "r").read().strip())))

def distribute(banks):
    seen = defaultdict(list)
    steps = 0
    seen[tuple(banks)].append(steps)
    while len(seen[tuple(banks)]) <= 2:
        steps = steps + 1
        max_index = banks.index(max(banks))
        full, remainder = divmod(banks[max_index], len(banks))
        banks[max_index] = 0
        extra_index = [value if value < len(banks) else value - len(banks) for value in range(max_index+1, max_index+remainder+1)]
        banks = [value + full + 1  if index in extra_index else value + full for index, value in enumerate(banks)]
        seen[tuple(banks)].append(steps)

    cycle = seen[tuple(banks)]
    part1 = cycle[1]
    part2 = cycle[2] - cycle[1]

    return part1, part2

part1, part2 = distribute(banks)

print(part1, part2)
