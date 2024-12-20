from functools import cache

Input = open("data/2024/dag 19. input.txt", "r").read().split("\n\n")

towels = Input[0].split(", ")
designs = Input[1].split("\n")[0:-1]


@cache
def next_towels(design):
    if len(design) == 0:
        return 1

    new_towels = [towel for towel in towels if design.startswith(towel)]
    if len(new_towels) == 0:
        return 0

    new_designs = [design[len(towel):] for towel in new_towels]
    res = [next_towels(new_design) for new_design in new_designs]

    return sum(res)


result = [next_towels(design) for design in designs]
part1 = sum([value > 0 for value in result])
part2 = sum(result)

print(part1, part2)
