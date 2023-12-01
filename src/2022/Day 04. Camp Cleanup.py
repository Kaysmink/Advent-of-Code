Input = open("data/dag 04. input.txt", "r").read().split("\n")[:-1]
ranges = [[list(map(int,values.split("-"))) for values in line.split(",")] for line in Input]

print(sum([(range1[0] >= range2[0] and range1[1] <= range2[1]) or ((range2[0] >= range1[0] and range2[1] <= range1[1])) for range1, range2 in ranges]))
print(sum([len(set.intersection(set(range(range1[0], range1[1] +1)), set(range(range2[0], range2[1] +1)))) > 0 for range1, range2 in ranges]))
