import re
from collections import defaultdict


Input = open("data/2015/dag 16. input.txt", "r").read().split("\n")[0:-1]
sues_list = [re.findall(r"(\d+|[a-z]+)", line)[1::] for line in Input]

main_sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
            'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

sues = defaultdict(dict)
for index, values in enumerate(sues_list):
    values = values[1::]
    for i in range(0,len(values),2):
        sues[index+1][values[i]] = int(values[i+1])

def check_sue(part, sue):
    if part == 1:
        return all([value == main_sue[property] for property, value in sue.items()])
    if part == 2:
        return all([value > main_sue[property] if property in ["cats", "trees"] else
                    value < main_sue[property] if property in ["pomeranians", "goldfish"] else
                    value == main_sue[property]
                    for property, value in sue.items()])


part1 = [sue_num for sue_num, properties in sues.items() if check_sue(1,properties)][0]
part2 = [sue_num for sue_num, properties in sues.items() if check_sue(2,properties)][0]

print(part1, part2)