from shapely import geometry, Point
from tqdm import tqdm

Input = open("data/2023/dag 10. input.txt", "r").read().split("\n")[0:-1]

maze = [list(line) for line in Input]
startpoint = [[xn, yn] for xn in range(0, len(Input[1])) for yn in range(0, len(Input)) if Input[yn][xn] == "S"][0]

# Looking at the maze, the only possible symbol for S is "7" since all others do not connect to 2 neighbors
maze[startpoint[1]][startpoint[0]] = "7"

step_dict = {"|": {"S": [0, 1], "N": [0, -1]},
             "-": {"E": [1, 0], "W": [-1, 0]},
             "L": {"S": [1, 0], "W": [0, -1]},
             "J": {"S": [-1, 0], "E": [0, -1]},
             "7": {"N": [-1, 0], "E": [0, 1]},
             "F": {"N": [1, 0], "W": [0, 1]}}

direction_dict = {"|": {"S": "S", "N": "N"},
                  "-": {"E": "E", "W": "W"},
                  "L": {"S": "E", "W": "N"},
                  "J": {"S": "W", "E": "N"},
                  "7": {"N": "W", "E": "S"},
                  "F": {"N": "E", "W": "S"}}


def walk_through_maze(current_possition, current_direction):
    visited = []
    while current_possition not in visited:
        visited.append(current_possition)

        current_symbol = maze[current_possition[1]][current_possition[0]]
        x, y = current_possition
        xn, yn = step_dict[current_symbol][current_direction]

        current_possition = [x+xn, y+yn]
        current_direction = direction_dict[current_symbol][current_direction]

    return visited


# part1
path = walk_through_maze(startpoint, "N")
part1 = len(path)//2

# Part 2
poly = geometry.Polygon([(x, y) for x, y in path])
part2 = sum([Point((xn, yn)).within(poly) for xn in tqdm(range(0, len(Input[1]))) for yn in range(0, len(Input))])

print(part1, part2)
