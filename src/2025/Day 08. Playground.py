import math
import re
from collections import defaultdict

Input = open("data/2025/dag 08. input.txt", "r").read().split("\n")[0:-1]
junctions = {index : list(map(int,re.findall(r"\d+", line))) for index, line in enumerate(Input)}
closest_junctions = sorted(set([(math.dist(j1, j2), tuple(sorted((index, index2)))) for index, j1 in junctions.items() for index2, j2 in junctions.items() if index != index2]))


def cluster_junctions(iterations):
    clusters = defaultdict(set)
    new_group = 0
    pair_num = 0
    seen = set()
    while closest_junctions:
        if pair_num == iterations:
            part1 = math.prod(sorted([len(values) for key, values in clusters.items()], reverse=True)[0:3])

        pair_num += 1
        dist, (j1, j2) = closest_junctions.pop(0)
        seen.update([j1,j2])

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
            clusters[new_group].update([j1,j2])
            new_group += 1

        if len(seen) == len(junctions) and len(clusters) == 1:
            part2 = junctions[j1][0] * junctions[j2][0]
            break

    return part1, part2


part1, part2 = cluster_junctions(1000)

print(part1, part2)