import regex as re

Input = open("data/2023/dag 05. input.txt", "r").read().split("\n\n")
seeds = list(map(int, re.findall(r'\d+', Input[0])))


def seed_to_location_map(value):
    for table in Input[1::]:
        value = map_value(value, table)

    return value


def map_value(value, mapping_table):
    mappings = [list(map(int, re.findall(r'\d+', line))) for line in mapping_table.split("\n")[1::]]

    result = value
    for dest, start, Range in mappings:
        if value >= start and value < start+Range:
            result = value + dest - start
            break

    return result


part1 = min([seed_to_location_map(seed) for seed in seeds])


"""
First i reversed the mappings so the result will be the seednumber for a given locations
"""


def reverse_map_value(value, mapping_table):
    mappings = [list(map(int, re.findall(r'\d+', line))) for line in mapping_table.split("\n")[1::]]

    result = value
    for dest, start, Range in mappings:
        if value >= dest and value < dest + Range:
            result = (start + value - dest)

    return result


def location_to_seed_map(value):
    for table in reversed(Input[1::]):
        value = reverse_map_value(value, table)

    return value


"""
I checked for a range of locations in increments of 100.000 if there was a hit in our seed ranges

the first location which had a seed which was included in our range was 27800001.

next i lowered the increments to 10.000, 1.000, 100, 10 and 1 till I finally had the smallest location with a

valid seed number
"""

seed_ranges = [[seeds[index], seeds[index] + seeds[index + 1]] for index in range(0, len(seeds), 2)]
part2 = 26829000
while True:
    seed = location_to_seed_map(part2)

    if any([seedMin <= seed <= seedMax for seedMin, seedMax in seed_ranges]):
        break
    part2 = part2 + 1


print(part1, part2)
