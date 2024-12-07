from copy import deepcopy as dc

Input = open("data/2024/dag 06. input.txt", "r").read().split("\n")[0:-1]
Input = [list(line) for line in Input]

current_position, current_direction = [[(x, y), Input[y][x]] for x in range(
    len(Input[0])) for y in range(len(Input)) if Input[y][x] in ["<", ">", "^", "v"]][0]

step_dict = {"^": [0, -1], ">": [1, 0], "v": [0, 1], "<": [-1, 0]}
new_direction_dict = {"^": ">", ">": "v", "v": "<", "<": "^"}


def walk_through_maze(Input, current_position, current_direction, new_block=False):
    if new_block:
        x, y = new_block
        Input = dc(Input)
        Input[y][x] = "#"

    visited = set()
    blocks = set()
    while True:
        visited.add(current_position)
        xn, yn = [a + b for a, b in zip(current_position, step_dict[current_direction])]

        if xn < 0 or xn >= len(Input[0]) or yn < 0 or yn >= len(Input):
            break

        if Input[yn][xn] == "#":
            if (xn, yn, current_direction) in blocks:
                return "LOOP"

            blocks.add((xn, yn, current_direction))
            current_direction = new_direction_dict[current_direction]
            continue

        current_position = (xn, yn)

    return len(visited)


part1 = walk_through_maze(Input, current_position, current_direction)

# Part 2
new_blocks = [(x, y) for x in range(
    len(Input[0])) for y in range(len(Input)) if Input[y][x] not in ["#", "<", ">", "^", "v"]]

part2 = [walk_through_maze(Input, current_position, current_direction, new_block) for new_block in new_blocks]

print(part1, part2.count("LOOP"))
