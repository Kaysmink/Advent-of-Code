from itertools import groupby

number = open("data/2015/dag 10. input.txt", "r").read().strip()


def look_and_say(number):
    counter = [(char, str(sum(1 for _ in group))) for char, group in groupby(number)]
    result = "".join([count+num for num, count in counter])

    return result

for play in range(50):
    number = look_and_say(number)
    if play == 39:
        part1 = len(number)

part2 = len(number)

print(part1, part2)
