from itertools import combinations

containers = tuple(list(map(int,open("data/2015/dag 17. input.txt", "r").read().split("\n")[0:-1])))

combinations = [comb for n in range(1,len(containers)+1) for comb in combinations(containers, n) if sum(comb) == 150]

part1 = len(combinations)
part2 = len([c1 for c1 in combinations if len(c1) == min([len(c2) for c2 in combinations])])

print(part1, part2)