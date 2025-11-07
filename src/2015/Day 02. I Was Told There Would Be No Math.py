import re
import numpy as np

Input = open("data/2015/dag 02. input.txt", "r").read().split("\n")[0:-1]
presents = [list(map(int,re.findall(r'[\d]+', line))) for line in Input]

part1 = sum([2*l*w + 2*w*h + 2*h*l + np.prod(sorted([l,w,h])[0:-1]) for l,w,h in presents])
part2 = sum([sum(sorted([l,w,h])[0:-1]) *2 + l*w*h for l,w,h in presents])

print(part1, part2)


