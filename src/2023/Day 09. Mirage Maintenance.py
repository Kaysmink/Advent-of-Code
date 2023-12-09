import numpy as np

Input = open("data/2023/dag 09. input.txt", "r").read().split("\n")[0:-1]
sequences = [[int(number) for number in line.split(" ")] for line in Input]


def get_differences(seq, index):
    values = [seq[index]]
    while not all([number == 0 for number in seq]):
        seq = np.diff(seq)
        values.append(seq[index])
    return values


def get_previous_number(seq):
    value = 0
    for first in seq[::-1]:
        value = first - value
    return value


dif_first = [get_differences(seq, 0) for seq in sequences]
dif_last = [get_differences(seq, -1) for seq in sequences]

part1 = sum([sum(seq) for seq in dif_last])
part2 = sum([get_previous_number(seq) for seq in dif_first])

print(part1, part2)
