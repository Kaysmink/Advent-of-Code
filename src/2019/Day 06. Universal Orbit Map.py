from collections import defaultdict

Input = open("data/2019/dag 06. input.txt", "r").read().split("\n")[0:-1]
Input = [line.split(")") for line in Input]

objects = defaultdict(list)
[objects[o2].append(o1) for o1, o2 in Input]


def count_orbits(object):
    if object not in objects.keys():
        return 0

    return 1 + sum([count_orbits(new_object) for new_object in objects[object]])


def shortest_path(current_poss, end):
    visited = []
    step = 0
    while current_poss:
        visited.extend(current_poss)
        new_poss = [objects[poss] for poss in current_poss]
        current_poss = [value for sub in new_poss for value in sub if value not in visited]

        step += 1
        if end in current_poss:
            return step


part1 = sum([count_orbits(object) for object in objects])

objects = defaultdict(list)
[objects[o2].append(o1) for o1, o2 in Input]
[objects[o1].append(o2) for o1, o2 in Input]

part2 = shortest_path(objects["YOU"], objects["SAN"][0])

print(part1, part2)