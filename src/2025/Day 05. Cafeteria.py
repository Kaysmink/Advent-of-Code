import re

ranges, ingredients = open("data/2025/dag 05. input.txt", "r").read().split("\n\n")
ingredients = list(map(int,ingredients.split("\n")[0:-1]))
ranges = [list(map(int,re.findall(r"\d+", line))) for line in ranges.split("\n")]

def check_ingredient(ingredient):
    for n1, n2 in ranges:
        if n1 <= ingredient <= n2:
            return True
    return False


def get_ingredient(ranges):
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

    return sum(end - start + 1 for start, end in seen)


part1 = sum([check_ingredient(ingredient) for ingredient in ingredients])
part2 = get_ingredient(ranges)

print(part1, part2)