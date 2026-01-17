import re
from collections import deque, defaultdict

instructions = open("data/2017/dag 16. input.txt", "r").read().strip().split(",")

def swap(dance_order, i1,i2):
    dance_order = list(dance_order)
    dance_order[i1], dance_order[i2] = dance_order[i2], dance_order[i1]

    return deque(dance_order)

def execute_dance(instructions, dances):
    dance_order = deque("abcdefghijklmnop")
    dance_order_dict = defaultdict(list)

    for dance in range(dances):
        for instruction in instructions:
            if instruction[0] == "s":
                value = int(instruction[1:])
                dance_order.rotate(value)
            if instruction[0] == "x":
                i1, i2 = re.findall(r"\d+", instruction[1:])
                dance_order = swap(dance_order, int(i1), int(i2))
            if instruction[0] == "p":
                dance_order = swap(dance_order, dance_order.index(instruction[1]), dance_order.index(instruction[3]))

        if dance == 0:
            part1 = "".join(list(dance_order))

        dance_order_dict["".join(list(dance_order))].append(dance)

    return part1, dance_order_dict

part1, dance_order_dict = execute_dance(instructions, 100)

# after 36 seconds the dance_order is back to the start.
# so the result of dance 1.000.000.000 is the same as dance (1000000000)%36 -1 = 27)
part2 = [key for key, value in dance_order_dict.items() if 27 in value][0]

print(part1, part2)