import re
from collections import defaultdict
from copy import deepcopy
from functools import cache
from itertools import product


Input = open("data/2022/dag 16. input.txt", "r").read().split("\n")[0:-1]
tunnels = [re.findall(r"[A-Z]{2}|\d+", line) for line in Input]
tunnel_dict = {tunnel[0]:{"rate":int(tunnel[1]), "tunnels":tunnel[2:]} for tunnel in tunnels}

@cache
def calculate_pressure(valves):
    return sum([tunnel_dict[valve]["rate"] for valve in valves])

def walk_through_pipes(current_states, minutes):
    number_of_valves = sum([tunnel_dict[valve]["rate"] > 0 for valve in tunnel_dict.keys()])

    seen = defaultdict(int)
    minute = 0
    while minute < minutes:
        print(minute, len(current_states))
        minute = minute + 1
        new_states = defaultdict(list)
        for tunnel, open, pressure in current_states:
            new_pressure = pressure + calculate_pressure(open)
            seen[(tunnel, open)] = pressure
            if len(open) == number_of_valves:
                new_open = deepcopy(open)
                new_states[(tunnel, new_open)].append(new_pressure)
            else:
                next_tunnels = tunnel_dict[tunnel]["tunnels"]
                for next_tunnel in next_tunnels:
                    new_open = deepcopy(open)
                    new_states[(next_tunnel, new_open)].append(new_pressure)

                if tunnel not in open and tunnel_dict[tunnel]["rate"] > 0:
                    new_open = deepcopy(open)
                    new_open = tuple(sorted(new_open + tuple([tunnel])))
                    new_states[(tunnel, new_open)].append(new_pressure)

        new_states = {(tunnel, open, max(values)) for (tunnel, open), values in new_states.items()}
        current_states = new_states

    return max([value for tunnel, open, value in current_states])

def walk_through_pipes_part2(current_states, minutes):
    number_of_valves = sum([tunnel_dict[valve]["rate"] > 0 for valve in tunnel_dict.keys()])

    seen = defaultdict(int)
    minute = 0
    while minute < minutes:
        print(minute, len(current_states))
        minute = minute + 1
        new_states = defaultdict(list)
        for (t1,t2), open, pressure in current_states:
            seen[((t1,t2), open)] = pressure
            if len(open) == number_of_valves:
                new_open = deepcopy(open)
                new_pressure = pressure + calculate_pressure(open)
                new_states[(("X", "X"), new_open)].append(new_pressure)
            else:
                next_t1 = tunnel_dict[t1]["tunnels"]
                next_t2 = tunnel_dict[t2]["tunnels"]

                poss_steps = [comb for comb in product(next_t1+[t1], next_t2+[t2])]
                for new_t1, new_t2 in poss_steps:
                    new_open = deepcopy(open)
                    new_pressure = pressure + calculate_pressure(open)
                    if new_t1 == t1 and new_t1 not in open and tunnel_dict[new_t1]["rate"] > 0:
                        new_open = tuple(sorted(new_open + tuple([new_t1])))
                    if new_t2 == t2 and new_t2 not in open and tunnel_dict[new_t2]["rate"] > 0:
                        if new_t1 != new_t2:
                            new_open = tuple(sorted(new_open + tuple([new_t2])))

                    new_pos = tuple(sorted([new_t1, new_t2]))
                    new_states[(new_pos, new_open)].append(new_pressure)

        new_states = {(tunnel, open, max(values)) for (tunnel, open), values in new_states.items()}

        max_value = max([value for tunnel, open, value in new_states])
        new_states =  {(tunnel, open, value) for (tunnel, open, value) in new_states if value >= max_value - 208}
        current_states = new_states

    return max([value for tunnel, open, value in current_states])

start = ("AA",tuple(), 0)
current_states = [start]

part1 = walk_through_pipes(current_states, 30)

start = (("AA", "AA"),tuple(), 0)
current_states = [start]

part2 = walk_through_pipes_part2(current_states, 26)

print(part1, part2)