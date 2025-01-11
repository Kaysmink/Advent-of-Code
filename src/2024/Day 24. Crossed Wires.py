import re

Input = open("data/2024/dag 24. input.txt", "r").read().split("\n\n")
# Input = open("data/2024/test.txt", "r").read().split("\n\n")

wires = [line.split(": ") for line in Input[0].split("\n")]
known_wires = {wire: value for wire, value in wires}
connections = re.findall(r'([\S]{3}) (XOR|OR|AND) ([\S]{3}) -> ([\S]{3})', Input[1])

operator_dict = {"XOR": "^", "OR": "or", "AND": "and"}


def check_connections(connections):
    while connections:
        unknown_connections = []
        for w1, operator, w2, w3 in connections:
            if w1 in known_wires.keys() and w2 in known_wires:
                known_wires[w3] = str(eval(known_wires[w1] + " " + operator_dict[operator] + " " + known_wires[w2]))
            else:
                unknown_connections.append((w1, operator, w2, w3))
        connections = unknown_connections


check_connections(connections)

zWires = sorted([[key, value] for key, value in known_wires.items() if key.startswith("z")], reverse=True)
part1 = int("".join([value for wire, value in zWires]), 2)

print(part1)

xy_connections = [(w1, operator, w2, w3) for w1, operator, w2, w3 in connections if
                  w1.startswith(("x", "y")) and w2.startswith(("x", "y"))]
