import math
import re
from collections import defaultdict
from copy import deepcopy
import networkx as nx

Input = open("data/2023/dag 25. input.txt", "r").read().split("\n")
links = [re.findall(r"[a-z]{3}", line) for line in Input]

def create_link_dict():
    link_dict = defaultdict(list)
    for link in links:
        for c in link[1:]:
            link_dict[link[0]].append(c)
            link_dict[c].append(link[0])

    return link_dict


def cluster_cliques(links, remove_wires):
    links = deepcopy(links)
    for wire in remove_wires:
        links.remove(wire)

    clusters = defaultdict(set)
    new_group = 0
    seen = set()
    while links:
        j1,j2 =  links.pop()
        seen.update([j1, j2])

        cluster1 = [key for key, cluster in clusters.items() if j1 in cluster]
        cluster2 = [key for key, cluster in clusters.items() if j2 in cluster]

        if cluster1 and cluster2:
            if cluster1 == cluster2:
                continue
            clusters[cluster1[0]].update(clusters[cluster2[0]])
            del clusters[cluster2[0]]
        if cluster1 and not cluster2:
            clusters[cluster1[0]].add(j2)
        if cluster2 and not cluster1:
            clusters[cluster2[0]].add(j1)
        if not cluster1 and not cluster2:
            clusters[new_group].update([j1, j2])
            new_group += 1

    return clusters


link_dict = create_link_dict()
all_links = {tuple(sorted((c1,c2))) for c1, values in link_dict.items() for c2 in values}


# create and draw graph and search for 3 wires to disconnect
graph = nx.Graph()
create_nodes = [graph.add_node(node) for node in link_dict.keys()]

for n1, value in link_dict.items():
    for n2 in value:
        graph.add_edge(n1, n2)

nx.draw_networkx(graph)

clusters = cluster_cliques(all_links, [("lmj", "xgs"), ("hgk", "pgz"), ("gzr", "qnz")])
part1 = math.prod([len(cluster) for cluster in clusters.values()])

print(part1)


