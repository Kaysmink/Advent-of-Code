from collections import defaultdict

import regex as re


Input = open("data/2023/dag 15. input.txt", "r").read().split("\n")[0].split(",")


def hash_score(string):
    result = 0
    for char in string:
        result = ((result + ord(char)) * 17) % 256

    return result


def perform_step(step):
    label, hash = [step[0], hash_score(step[0])]
    current_index = [index for index, value in enumerate(box_dict[hash]) if re.findall(label, value)]

    if step[1] == "=":
        if current_index:
            box_dict[hash][current_index[0]] = label + " " + step[2]
        else:
            box_dict[hash].append(label + " " + step[2])
    if step[1] == "-":
        if current_index:
            box_dict[hash].pop(current_index[0])


def get_power(box_dict):
    result = 0
    for key, value in box_dict.items():
        if value:
            for index, lens in enumerate(value):
                length = int(re.findall(r'\d+', lens)[0])
                result = result + (1 + int(key)) * (index + 1) * length

    return result


# Part 1
part1 = sum([hash_score(string) for string in Input])

# Part 2
box_dict = defaultdict(list)
labels = [re.findall(r'\w+|[=|-]|[\d]+', string) for string in Input]

for step in labels:
    perform_step(step)

part2 = get_power(box_dict)

print(part1, part2)
