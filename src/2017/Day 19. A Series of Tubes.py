Input = open("data/2017/dag 19. input.txt", "r").read().split("\n")[0:-1]
maze = {(x,y):Input[y][x] for x in range(len(Input[0])) for y in range(len(Input)) if Input[y][x] != " "}

direction_dict = {"v":[0,1],
                  "^":[0,-1],
                  ">":[1,0],
                  "<":[-1,0]}

def get_neighbors(x,y):
    return [(xn, yn) for xn in range(x-1, x+2) for yn in range(y-1, y+2) if
            (xn,yn) in maze.keys() and (abs(x - xn) + abs(y - yn) == 1)]

def get_new_direction(pos, direction):
    neighbors = get_neighbors(*pos)
    if direction in ["^", "v"]:
        xn,yn = [(x,y) for (x,y) in neighbors if x != pos[0]][0]
        return "<" if xn < pos[0] else ">"
    if direction in ["<", ">"]:
        xn,yn = [(x,y) for (x,y) in neighbors if y != pos[1]][0]
        return "^" if yn < pos[1] else "v"

def walk_maze():
    pos = [(x,y) for (x,y), value in maze.items() if y == 0][0]
    direction = "v"

    visited_letters = []
    steps = 1
    while True:
        pos = tuple([sum(v) for v in zip(pos, direction_dict[direction])])
        if pos not in maze.keys():
            break
        if maze[pos] not in ["|", "-", "+"]:
            visited_letters.append(maze[pos])
        if maze[pos] == "+":
            direction = get_new_direction(pos, direction)

        steps = steps + 1

    return "".join(visited_letters), steps

part1, part2 = walk_maze()

print(part1, part2)