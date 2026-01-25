import re
from collections import defaultdict

Input = open("data/2017/dag 24. input.txt", "r").read().split("\n")[0:-1]
ports_dict = {index: list(map(int, re.findall("\d+", line))) for index, line in enumerate(Input)}

pins_dict = defaultdict(set)
[pins_dict[pin].add(port) for port, pins in ports_dict.items() for pin in pins]

def combine_ports(ports, pin):
    next_ports = [port for port in pins_dict[pin] if port not in ports]
    if not next_ports:
        bridges.append([len(ports), sum([sum(ports_dict[port]) for port in ports])])

    new_states = [[ports + tuple([port]),
                  [value for value in ports_dict[port] if value != pin][0] if ports_dict[port].count(pin) ==1 else pin]
                  for port in next_ports]

    return [combine_ports(*state) for state in new_states]

bridges = []
start_ports = [[tuple([port]), max(ports_dict[port])] for port in pins_dict[0]]
[combine_ports(*start) for start in start_ports]

part1 = max(bridges, key=lambda x: x[1])[1]
max_l = max(bridges, key=lambda x: x[0])[0]
part2 = max([s for l,s in bridges if l == max_l])

print(part1, part2)