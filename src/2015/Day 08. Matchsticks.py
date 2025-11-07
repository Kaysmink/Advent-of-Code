import re

Input = open("data/2015/dag 08. input.txt", "r").read().split("\n")[0:-1]


def decode(string):
    special_tokens = re.findall(r"(\\x[0-9a-f]{2}|\\\\|\\\")", string)
    result = sum([3 if "x" in token else 1 for token in special_tokens]) + 2

    return result


def encode(string):
    special_tokens = re.findall(r"(\"|\\)", string[1:-1])

    result = len(special_tokens) + 4
    return result


part1 = sum([decode(string) for string in Input])
part2 = sum([encode(string) for string in Input])

print(part1, part2)
