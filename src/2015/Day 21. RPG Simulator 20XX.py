import re
from itertools import combinations, product

hitpoints_boss, damage_boss, armor_boss = list(map(int,re.findall(r"\d+", open("data/2015/dag 21. input.txt", "r").read())))

weapons = {0:[0,0,0], 1:[8,4,0], 2:[10,5,0], 3:[25,5,0], 4:[40,7,0], 5:[74,8,0]}
armors = {0:[0,0,0], 1:[13,0,1], 2:[31,0,2], 3:[53,0,3], 4:[75,0,4], 5:[102,0,5]}
rings = {0:[0,0,0], 1:[25,1,0], 2:[50,2,0], 3:[100,3,0], 4:[20,0,1], 5:[40,0,2], 6:[80,0,3]}

def buy_combinations(part, w,a,r):
    chosen_weapons = [comb for n in range(1,w+1) for comb in combinations([1,2,3,4,5], n)]
    chosen_armors = [comb for n in range(1,a+1) for comb in combinations([1,2,3,4,5], n)]
    chosen_rings = [comb for n in range(1,r+1) for comb in combinations([1,2,3,4,5,6], n)]

    if part == 1:
        chosen_armors = chosen_armors + [tuple([0])]
        chosen_rings = chosen_armors + [tuple([0])]

    combs = [comb for comb in product(chosen_weapons, chosen_armors, chosen_rings)]

    return combs


def fight(items):
    weapon, armor, ring = items
    costs = sum([weapons[w][0] for w in weapon] + [armors[a][0] for a in armor] + [rings[r][0] for r in ring])
    damage_p = sum([weapons[w][1] for w in weapon] + [armors[a][1] for a in armor] + [rings[r][1] for r in ring])
    armor_p = sum([weapons[w][2] for w in weapon] + [armors[a][2] for a in armor] + [rings[r][2] for r in ring])

    hitpoints_p = 100
    hitpoints_b, damage_b, armor_b = hitpoints_boss, damage_boss, armor_boss
    while True:
        hitpoints_b = hitpoints_b - max(damage_p - armor_b,1)
        if hitpoints_b <= 0:
            return costs, True

        hitpoints_p = hitpoints_p - max(damage_b - armor_p,1)
        if hitpoints_p <= 0:
            return costs, False


games_part1 = [fight(items) for items in buy_combinations(1,1,1,2)]
games_part2 = [fight(items) for items in buy_combinations(2,5,5,6)]

part1 = min([cost for cost, winner in games_part1 if winner])
part2 = max([cost for cost, winner in games_part2 if not winner])

print(part1, part2)
