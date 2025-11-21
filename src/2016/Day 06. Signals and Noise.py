from collections import Counter

Input = open("data/2016/dag 06. input.txt", "r").read().split("\n")[0:-1]

part1 = "".join([char for char, freq in (sorted(Counter(index).items(), key=lambda x: -x[1])[0] for index in map(list, zip(*Input)))])
part2 = "".join([char for char, freq in (sorted(Counter(index).items(), key=lambda x: x[1])[0] for index in map(list, zip(*Input)))])

print(part1, part2)