from copy import deepcopy

Input = open("data/2023/dag 13. input.txt", "r").read().split("\n\n")[0:-1]
patterns = [[line for line in pattern.split("\n")] for pattern in Input]

replace_dict = {".": "#",
                "#": "."}


def check_rows(pattern, excluding=[False, -1]):
    for y in range(0, len(pattern) - 1):
        if excluding[0] == "row" and excluding[1] == y:
            continue

        result = all([pattern[y - i] == pattern[y + 1 + i] for i in range(0, y + 1) if y + 1 + i < len(pattern)])
        if result:
            return y

    return -1


def check_cols(pattern, excluding=[False, -1]):
    cols = [[row[x] for row in pattern] for x in range(0, len(pattern[0]))]

    for x in range(0, len(cols) - 1):
        if excluding[0] == "col" and excluding[1] == x:
            continue

        result = all([cols[x - i] == cols[x + 1 + i] for i in range(0, x + 1) if x + 1 + i < len(cols)])
        if result:
            return x

    return -1


def get_pattern_score(pattern, excluding=[False, -1]):
    row_index = check_rows(pattern, excluding)
    if row_index >= 0:
        return 100 * (row_index + 1)

    col_index = check_cols(pattern, excluding)
    if col_index >= 0:
        return col_index + 1

    return -1


def find_diferent_mirror(pattern):
    old_score = get_pattern_score(pattern)
    exclude = ["col", old_score - 1] if old_score < 100 else ["row", int((old_score / 100) - 1)]
    pattern = [list(line) for line in pattern]

    for x in range(0, len(pattern[0])):
        for y in range(0, len(pattern)):
            new_pattern = deepcopy(pattern)
            new_pattern[y][x] = replace_dict[new_pattern[y][x]]
            new_pattern = ["".join(line) for line in new_pattern]
            new_score = get_pattern_score(new_pattern, excluding=exclude)
            if new_score != -1 and new_score != old_score:
                return new_score

    return -1


part1 = sum([get_pattern_score(pattern) for pattern in patterns])
part2 = sum([find_diferent_mirror(pattern) for pattern in patterns])

print(part1, part2)
