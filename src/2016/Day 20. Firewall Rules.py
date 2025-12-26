import re

Input = open("data/2016/dag 20. input.txt", "r").read().split("\n")[0:-1]
ranges = [list(map(int,re.findall(r"\d+", line))) for line in Input]

def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])

    seen = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            seen.append((current_start, current_end))
            current_start, current_end = start, end

    seen.append((current_start, current_end))

    return seen

ranges = merge_ranges(ranges)

part1 = ranges[0][1]+1
part2 = sum([ranges[i][0] - ranges[i-1][1] - 1 for i in range(1,len(ranges))])

print(part1, part2)