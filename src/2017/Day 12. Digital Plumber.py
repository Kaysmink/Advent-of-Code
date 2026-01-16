import re
from collections import defaultdict

Input = open("data/2017/dag 12. input.txt", "r").read().split("\n")[0:-1]
links = [re.findall(r"\d+", line) for line in Input]

def create_link_dict(links):
    link_dict = defaultdict(set)
    for link in links:
        for l2 in link[1:]:
            if link[0] != l2:
                link_dict[link[0]].add(l2)
                link_dict[l2].add(link[0])
    return link_dict


def get_group(pos):
    global seen

    neighbors = link_dict[pos]
    if not neighbors:
        return 1

    seen.add(pos)
    return sum(get_group(neighbors) for neighbors in neighbors if neighbors not in seen)

def find_all_groups():
    global seen

    positions = set([str(i) for i in range(2000)])
    groups = 0

    while positions:
        groups += 1
        seen = set()

        pos = positions.pop()
        if pos not in link_dict.keys():
            continue

        get_group(pos)

        if "0" in seen:
            part1 = len(seen)

        seen.remove(pos)
        for pos in seen:
            positions.remove(pos)

    return part1, groups

seen = set()
link_dict = create_link_dict(links)
program = get_group("0")

part1, part2 = find_all_groups()

print(part1, part2)