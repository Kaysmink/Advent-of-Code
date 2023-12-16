from collections import Counter


Input = open("data/2023/dag 14. input.txt", "r").read().split("\n")[0:-1]
cubes = [[xn, yn] for xn in range(0, len(Input[0])) for yn in range(0, len(Input)) if Input[yn][xn] == "#"]
circles = [[xn, yn] for xn in range(0, len(Input[0])) for yn in range(0, len(Input)) if Input[yn][xn] == "O"]


def find_next_cube_index(circle, cubes, direction):
    if direction in ["N", "W"]:
        poss_rocks = [rock for rock in cubes if rock < circle]
        if poss_rocks:
            return max(poss_rocks)
        else:
            return -1

    if direction in ["S", "E"]:
        poss_rocks = [rock for rock in cubes if rock > circle]
        if poss_rocks:
            return min(poss_rocks)
        else:
            return len(Input)


def move_rocks_vertical(circles, direction):
    new_coords_result = []
    for col_num in range(0, len(Input[0])):
        cube = [cube[1] for cube in cubes if cube[0] == col_num]
        circle = [circle[1] for circle in circles if circle[0] == col_num]

        closest_rocks = [find_next_cube_index(rock, cube, direction) for rock in circle]
        closest_rocks = Counter(closest_rocks)

        if direction == "N":
            new_circles = [list(range(key + 1, key + 1 + value)) for key, value in closest_rocks.items()]
        else:
            new_circles = [list(range(key - 1, key - 1 - value, -1)) for key, value in closest_rocks.items()]

        new_coords = [[col_num, value] for value in sum(new_circles, [])]
        new_coords_result.extend(new_coords)

    return new_coords_result


def move_rocks_horizontal(circles, direction):
    new_coords_result = []
    for row_num in range(0, len(Input)):
        cube = [cube[0] for cube in cubes if cube[1] == row_num]
        circle = [circle[0] for circle in circles if circle[1] == row_num]

        closest_rocks = [find_next_cube_index(rock, cube, direction) for rock in circle]
        closest_rocks = Counter(closest_rocks)

        if direction == "W":
            new_circles = [list(range(key + 1, key + 1 + value)) for key, value in closest_rocks.items()]
        else:
            new_circles = [list(range(key - 1, key - 1 - value, -1)) for key, value in closest_rocks.items()]

        new_coords = [[value, row_num] for value in sum(new_circles, [])]
        new_coords_result.extend(new_coords)

    return new_coords_result


"""
after running 200 iteration is became clear that after 95 iteration a cycle started with length 11
"""
result = []
for i in range(0, 200):
    circles = move_rocks_vertical(circles, "N")
    if i == 0:
        part1 = sum([len(Input) - y for x, y in circles])
    circles = move_rocks_horizontal(circles, "W")
    circles = move_rocks_vertical(circles, "S")
    circles = move_rocks_horizontal(circles, "E")

    result.append(sum([len(Input) - y for x, y in circles]))

part2 = result[94 + ((1000000000 - 95) % 11)]

print(part1, part2)
