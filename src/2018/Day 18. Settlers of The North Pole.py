from collections import defaultdict

Input = open("data/2018/dag 18. input.txt", "r").read().split("\n")[0:-1]
landscape = {(x,y):Input[y][x] for x in range(len(Input[0])) for y in range(len(Input))}

def get_new_value(landscape, x, y):
    neighbors = [landscape[(xn, yn)] for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
                 0 <= xn < 50 and 0 <= yn < 50 and (abs(x - xn) + abs(y - yn) > 0)]

    if landscape[(x,y)] == ".":
        return "|" if neighbors.count("|") >=3 else "."
    if landscape[(x,y)] == "|":
        return "#" if neighbors.count("#") >=3 else "|"
    if landscape[(x,y)] == "#":
        return "#" if neighbors.count("#") >=1 and neighbors.count("|") >=1 else "."

def change_landscape(landscape, seconds):
    score_dict = defaultdict(list)
    for second in range(seconds):
        landscape = {key:get_new_value(landscape, *key) for key, value in landscape.items()}
        score = list(landscape.values()).count("|") * list(landscape.values()).count("#")
        score_dict[score].append(second)
        if second == 9:
            part1 = score

    return part1, score_dict

part1, scores = change_landscape(landscape, 1000)

# after 476 seconds an endless loop of states starts with a length of 28 seconds.
# so the result of second 1.000.000.000 is the same as second (476 + (1000000-476)%28 -1 = 495)
part2 = [key for key, value in scores.items() if 495 in value][0]

print(part1, part2)