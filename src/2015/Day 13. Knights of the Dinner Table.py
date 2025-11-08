import re
from itertools import permutations

Input = open("data/2015/dag 13. input.txt", "r").read().split("\n")[0:-1]
relations = [re.findall(r"([a-zA-z]+) would (gain|lose) (\d+) happiness units by sitting next to ([a-zA-z]+)", line)[0] for line in Input]


def calculate_happiness(part):
    scores = {(p1 + " " + p2): int(value) if sign == "gain" else -int(value) for p1, sign, value, p2 in relations}
    persons = set([value.split(" ")[0] for value in scores.keys()])

    if part == 2:
        for p1 in persons:
            scores["me " + p1] = 0
            scores[p1 + " me"] = 0
        persons.add("me")

    poss_positions = [perm for perm in permutations(persons, len(persons))]
    happiness = max([sum([scores[(pos[i] + " " + pos[i-1])] + scores[(pos[i] + " " + pos[i+1])] if i != len(pos)-1 else
                 scores[(pos[i] + " " + pos[i-1])] + scores[(pos[i] + " " + pos[0])] for i,value in enumerate(pos)]) for pos in poss_positions])

    return happiness


part1 = calculate_happiness(1)
part2 = calculate_happiness(2)

print(part1, part2)



