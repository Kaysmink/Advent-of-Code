from copy import deepcopy as dc

Input = open("data/2024/dag 15. input.txt", "r").read().split("\n\n")

Map = [list(line) for line in Input[0].split("\n")]
moves = [value for sub in Input[1].split("\n")[0:-1] for value in sub]

boxes = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "O"]
walls = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "#"]
position1 = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "@"][0]

step_dict = {">": [1, 0],
             "<": [-1, 0],
             "^": [0, -1],
             "v": [0, 1]}


def make_map_part2(boxes, walls, current_position):
    new_boxes = []
    new_walls = []

    for x, y in boxes:
        new_boxes.append(((x*2, y), (x*2+1, y)))
    for x, y in walls:
        new_walls.extend([(x*2, y), (x*2+1, y)])

    new_position = (current_position[0]*2, current_position[1])

    return new_boxes, new_walls, new_position


def get_moving_boxes(current_position, direction, part=1):
    moving_boxes = []
    x, y = current_position
    base_layer = [current_position]

    while True:
        if part == 1:
            x = x + step_dict[direction][0]
            y = y + step_dict[direction][1]
            if (x, y) in boxes:
                moving_boxes.append((x, y))

            elif (x, y) in walls:
                return [False, False]

            else:
                return [(x, y), moving_boxes]
        if part == 2:
            poss_next_box = [(x+step_dict[direction][0], y+step_dict[direction][1]) for x, y in base_layer]
            new_boxes = [box for xn, yn in poss_next_box for box in boxes2 if (xn, yn) in box]

            hit_wall = any(poss in walls2 for poss in poss_next_box)

            if hit_wall:
                return [False, False]

            if len(new_boxes) == 0:
                return [(x, y), moving_boxes]

            moving_boxes.extend(new_boxes)
            if direction == "<":
                base_layer = [min([box for sub in new_boxes for box in sub])]
            if direction == ">":
                base_layer = [max([box for sub in new_boxes for box in sub])]
            if direction in ["^", "v"]:
                new_boxes = dc(new_boxes)
                base_layer = [box for sub in new_boxes for box in sub]


def get_new_positions(empty, boxes, direction, current_position, part):
    xw, yw = empty
    num_boxes = len(boxes)
    if part == 1:
        if direction == ">":
            new_positions = [(xw-n, yw) for n in range(0, num_boxes+1)]
        if direction == "<":
            new_positions = [(xw+n, yw) for n in range(0, num_boxes+1)]
        if direction == "^":
            new_positions = [(xw, yw+n) for n in range(0, num_boxes+1)]
        if direction == "v":
            new_positions = [(xw, yw-n) for n in range(0, num_boxes+1)]

        boxes = new_positions[0:-1]
        current_position = new_positions[-1]
    else:
        if direction == ">":
            boxes = [((c1[0]+1, c1[1]), (c2[0]+1, c2[1])) for c1, c2 in boxes]
            current_position = (current_position[0] + 1, current_position[1])
        if direction == "<":
            boxes = [((c1[0]-1, c1[1]), (c2[0]-1, c2[1])) for c1, c2 in boxes]
            current_position = (current_position[0] - 1, current_position[1])
        if direction == "^":
            boxes = [((c1[0], c1[1]-1), (c2[0], c2[1]-1)) for c1, c2 in boxes]
            current_position = (current_position[0], current_position[1]-1)
        if direction == "v":
            boxes = [((c1[0], c1[1]+1), (c2[0], c2[1]+1)) for c1, c2 in boxes]
            current_position = (current_position[0], current_position[1]+1)

    return [boxes, current_position]


for index, move in enumerate(moves):
    empty_pos, boxes_in_line = get_moving_boxes(position1, move, 1)
    if boxes_in_line != False:
        new_boxes, position1 = get_new_positions(empty_pos, boxes_in_line, move, position1, 1)

        boxes = [box for box in boxes if box not in boxes_in_line]
        boxes.extend(new_boxes)

part1 = sum([x + 100*y for x, y in boxes])


# Part 2
boxes = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "O"]
walls = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "#"]
pos = [(x, y) for x in range(len(Map[0])) for y in range(len(Map)) if Map[y][x] == "@"][0]

boxes2, walls2, position2 = make_map_part2(boxes, walls, pos)
boxes2, walls2, position2 = dc(boxes2), dc(walls2), dc(position2)

for index, move in enumerate(moves):
    empty_pos, boxes_in_line = get_moving_boxes(position2, move, 2)

    if boxes_in_line != False:
        boxes_in_line = list(set(boxes_in_line))
        new_boxes, position2 = get_new_positions(empty_pos, boxes_in_line, move, position2, 2)

        boxes2 = [box for box in boxes2 if box not in boxes_in_line]
        boxes2.extend(new_boxes)

part2 = sum([c1[0] + 100*c1[1] for c1, c2 in boxes2])

print(part1, part2)
