import re

Input = open("data/2015/dag 06. input.txt", "r").read().split("\n")[0:-1]
instructions = [re.findall(r"off|on|toggle|\d+", line) for line in Input]

def lightshow(instructions):
    lights = {(x, y): False for x in range(1000) for y in range(1000)}
    brightness = {(x, y): 0 for x in range(1000) for y in range(1000)}

    for instruction in instructions:
        x1, y1, x2, y2 = list(map(int,instruction[1::]))
        rect = set([(x, y) for x in range(min(x1, x2), max(x1, x2) + 1) for y in range(min(y1, y2), max(y1, y2) + 1)])
        if instruction[0] == "on":
            for x,y in rect:
                lights[(x,y)] = True
                brightness[(x,y)] = brightness[(x,y)] + 1
        if instruction[0] == "off":
            for x,y in rect:
                lights[(x,y)] = False
                brightness[(x, y)] = max(brightness[(x, y)] - 1,0)
        if instruction[0] == "toggle":
            for x,y in rect:
                lights[(x,y)] = not lights[(x,y)]
                brightness[(x, y)] = brightness[(x, y)] + 2

    return sum(lights.values()), sum(brightness.values())

part1, part2 = lightshow(instructions)

print(part1, part2)






