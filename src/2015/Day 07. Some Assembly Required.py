import re

Input = open("data/2015/dag 07. input.txt", "r").read().split("\n")[0:-1]
instructions = [re.findall(r"(AND|OR|RSHIFT|LSHIFT|NOT|[a-z]{1,2}|\d+)", line) for line in Input]

instruction = {line[-1]:re.search(r"(AND|OR|RSHIFT|LSHIFT|NOT)", " ".join(line[0:-1])) for line in instructions}
instruction = {key:value.group() if value else None for key, value in instruction.items()}

wires = [re.findall(r"([a-z]{1,2}|\d+)", line) for line in Input]
wires = {line[-1]:int(line[0]) if line[0].isnumeric() and len(line[0:-1]) == 1 else line[0:-1] for line in wires}

wires_part2 = wires.copy()

calc = {"AND":"n1 & n2",
        "OR":"n1 | n2",
        "LSHIFT":"n1 << n2",
        "NOT":"~n1 & 0xFFFF",
        "RSHIFT":"n1 >> n2"}


def calc_result(instruction, values):
    if instruction == None:
        return values[0]

    if instruction == "NOT":
        n1 = int(values[0])
    else:
        n1,n2 = list(map(int,values))

    result = eval(calc[instruction])

    return result


def calculate_new_wires():
    for key, values in wires.items():
        if key not in known_wires:
            if all([str(value).isnumeric() for value in values]):
                wires[key] = calc_result(instruction[key], values)


def replace_known_wires(new_known):
    for known in new_known:
        for key, value in wires.items():
            if value.__class__ == list:
                wires[key] = [wires[known] if vn == known else vn for vn in value]
    known_wires.extend(new_known)


def run():
    global wires
    global known_wires

    known_wires = []

    while any([value.__class__ == list for value in wires.values()]):
        new_known = [key for key, value in wires.items() if value.__class__ != list and key not in known_wires]
        replace_known_wires(new_known)
        calculate_new_wires()

    return wires["a"]


part1 = run()

wires_part2["b"] = part1
wires = wires_part2.copy()
part2 = run()

print(part1, part2)
