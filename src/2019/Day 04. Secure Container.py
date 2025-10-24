import re
from itertools import groupby

Input = open("data/2019/dag 04. input.txt", "r").read()
xMin, xMax = re.findall(r'\d+', Input)

def check_number(part, number):
    if list(number) != sorted(number):
        return False
    if part == 1:
        if not re.search(r"(.)\1", number):
            return False
    if part == 2:
        if 2 not in [sum(1 for _ in group) for char, group in groupby(number)]:
            return False

    return True

part1 = len([number for number in range(int(xMin), int(xMax) + 1) if check_number(1, str(number))])
part2 = len([number for number in range(int(xMin), int(xMax) + 1) if check_number(2, str(number))])

print(part1, part2)
