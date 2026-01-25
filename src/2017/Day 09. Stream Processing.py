import numpy as np

Input = open("data/2017/dag 09. input.txt", "r").read().strip()

def process_garbage(string):
    removed_garbage = 0
    string = list(string)
    while "!" in string:
        index = string.index("!")
        del string[index:index+2]

    while "<" in string and ">" in string:
        i1, i2 = string.index("<"), string.index(">")
        removed_garbage = removed_garbage + (i2-i1-1)
        del string[i1:i2+1]

    string = "".join(string).replace(",", "")
    groups = np.cumsum([1 if char == "{" else -1 for char in string])
    score = sum([dim for sign, dim in zip(string, groups) if sign == "{"])

    return score, removed_garbage

part1, part2 = process_garbage(Input)

print(part1, part2)