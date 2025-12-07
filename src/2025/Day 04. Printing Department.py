Input = open("data/2025/dag 04. input.txt", "r").read().split("\n")[0:-1]
rolls = {(x,y) for x in range(len(Input[0])) for y in range(len(Input)) if Input[y][x] == "@"}


def get_neighbors(x, y, rolls):
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            (xn,yn) in rolls and (abs(x - xn) + abs(y - yn) != 0)]


def remove_rolls(part, rolls):
    result = 0
    while True:
        rem_rolls = set()
        for x, y in rolls:
            if len(get_neighbors(x, y, rolls)) < 4:
                rem_rolls.add((x, y))

        result = result + len(rem_rolls)
        rolls = rolls - rem_rolls

        if len(rem_rolls) == 0 or part == 1:
            break

    return result


part1, part2 = [remove_rolls(part, rolls) for part in [1,2]]

print(part1, part2)