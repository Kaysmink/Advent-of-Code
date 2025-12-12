import re
from functools import cache

Input = open("data/2025/dag 11. input.txt", "r").read().split("\n")[0:-1]
connections = [re.findall(r"[a-z]{3}", line) for line in Input]
connections = {line[0]:line[1::] for line in connections}

@cache
def find_paths(part, start):
    pos, b1, b2 = start
    if part == 1:
        if pos == "out":
            return 1
        return sum([find_paths(1, (new_pos, b1, b2)) for new_pos in connections[pos]])

    if part == 2:
        if start == ("out", True, True):
            return 1
        if pos == "out":
            return 0

        new_paths = [(new_pos, True, b2) if new_pos == "fft" else (new_pos, b1, True) if new_pos == "dac" else (new_pos, b1, b2) for new_pos in connections[pos]]
        return sum([find_paths(2, new_path) for new_path in new_paths])


part1 = find_paths(1, ("you", False, False))
part2 = find_paths(2, ("svr", False, False))

print(part1, part2)