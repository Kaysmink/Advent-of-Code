Input = open("data/2024/dag 01. input.txt", "r").read().split("\n")[0:-1]
Input = [list(map(int, line.split())) for line in Input]

l1 = sorted([value1 for value1, value2 in Input])
l2 = sorted([value2 for value1, value2 in Input])

part1 = sum([abs(l1[x] - l2[x]) for x in range(len(l1))])
part2 = sum([value * l2.count(value) for value in l1])

print(part1, part2)
