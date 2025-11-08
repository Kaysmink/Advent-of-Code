import re

Input = open("data/2015/dag 12. input.txt", "r").read().strip()
variables = eval(Input)

def parse_obj(obj):
    if obj.__class__ == int:
        return obj

    elif obj.__class__ == dict:
        return 0 if "red" in obj.values() else sum([parse_obj(child) for child in obj.values()])

    elif obj.__class__ == list:
        return sum([parse_obj(child) for child in obj])
    else:
        return 0


part1 = sum(list(map(int, re.findall(r"[-\d]+", Input))))
part2 = parse_obj(variables)

print(part1, part2)