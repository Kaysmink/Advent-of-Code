import re
from collections import defaultdict

Input = open("data/2017/dag 07. input.txt", "r").read().split("\n")[0:-1]

links = [re.findall(r"[a-z]+|\d+", line) for line in Input]
weights = {link[0]:int(link[1]) for link in links}

link_dict = defaultdict(list)
create_links = [link_dict[link[0]].append(l2) for link in links for l2 in link[2:] if len(link) > 2]

def calculate_weights(node):
    if node not in link_dict:
        return weights[node]

    return sum([calculate_weights(neighbor) for neighbor in link_dict[node]]) + weights[node]

def find_unbalance(root):
    while True:
        neighbors = link_dict[root]
        weight = [calculate_weights(neighbor) for neighbor in neighbors]
        if len(set(weight)) == 1:
            break
        value_needed = [v for v in weight if weight.count(v) > 1][0]
        root = neighbors[weight.index([v for v in weight if weight.count(v) == 1][0])]

    return weights[root] - (weights[root] + sum(weight) - value_needed)

part1 = sorted([(node, calculate_weights(node)) for node in weights.keys()], key = lambda x:x[1], reverse=True)[0][0]
part2 = find_unbalance(part1)

print(part1, part2)