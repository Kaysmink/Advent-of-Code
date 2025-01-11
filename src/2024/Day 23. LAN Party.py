import re
from collections import defaultdict
import networkx
from networkx.algorithms.clique import find_cliques


Input = open("data/2024/dag 23. input.txt", "r").read()
comps = set(re.findall(r"[a-z]{2}", Input))


def create_link_dict():
    link_dict = defaultdict()
    for c1 in comps:
        link = re.findall(r"([a-z]{2})"+"-"+c1, Input)
        link.extend(re.findall(c1+"-"+r"([a-z]{2})", Input))
        link_dict[c1] = link

    return link_dict


def get_network(n):
    result = []
    for c1 in comps:
        poss_c2 = link_dict[c1]
        for c2 in poss_c2:
            poss_c3 = link_dict[c2]
            poss_c3 = [poss for poss in poss_c3 if poss in link_dict[c1]]
            for c3 in poss_c3:
                if c1[0] == "t" or c2[0] == "t" or c3[0] == "t":
                    result.append([c1, c2, c3])
    return result


link_dict = create_link_dict()
part1 = len(get_network(3))//6


graph = networkx.Graph()
create_nodes = [graph.add_node(node) for node in link_dict.keys()]

for n1, value in link_dict.items():
    for n2 in value:
        graph.add_edge(n1, n2)

part2 = ",".join(sorted(sorted(find_cliques(graph), key=len)[-1]))

print(part1, part2)
