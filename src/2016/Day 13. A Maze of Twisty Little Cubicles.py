Input = int(open("data/2016/dag 13. input.txt", "r").read())

def get_value(x,y):
    return bin(x*x + 3*x + 2*x*y + y + y*y + Input)[2:].count("1") % 2 != 0

def create_maze(dim):
    maze = set([(x,y) for x in range(dim) for y in range(dim) if get_value(x,y)])

    return maze

def get_neighbors(x, y):
    return [(xn, yn) for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            0 <= xn < 50 and 0 <= yn < 50 and (abs(x - xn) + abs(y - yn) == 1)]

def walk_through_maze(current_positions, end):
    visited = set()
    steps = 0
    while current_positions:
        steps = steps + 1
        new_positions = []
        for x, y in current_positions:
            neighbors = get_neighbors(x,y)
            for neighbor in neighbors:
                if neighbor in maze:
                    continue
                if neighbor not in visited:
                    new_positions.append(neighbor)
                    visited.add(neighbor)
                if neighbor == end:
                    return steps, part2

        if steps == 50:
            part2 = len(visited)

        current_positions = new_positions

maze = create_maze(50)
part1, part2 = walk_through_maze([(1,1)], (31,39))

print(part1, part2)