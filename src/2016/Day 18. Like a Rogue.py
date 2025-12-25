from tqdm import tqdm

Input = open("data/2016/dag 18. input.txt", "r").read().strip()

def get_tile(x, row):
    return "".join([row[x-1] if x-1 >=0 else ".", row[x], row[x+1] if x+1 < len(row) else "."])

def get_new_row(prev_row):
    return "".join(["^" if get_tile(x,prev_row) in ["^^.", ".^^", "^..", "..^"] else "." for x in range(len(prev_row))])

def get_maze(row1, row2):
    maze = [Input]
    for row_num in tqdm(range(row2)):
        if row_num == row1:
            part1 = [value for sub in maze for value in sub].count(".")
        maze.append(get_new_row(maze[-1]))

    part2 = [value for sub in maze for value in sub].count(".")

    return part1, part2

part1, part2 = get_maze(39,399999)

print(part1, part2)