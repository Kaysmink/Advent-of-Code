Input = open("data/2024/dag 25. input.txt", "r").read().split("\n\n")  # manually removed last empty line in input file
Input = [line.split("\n") for line in Input]

patterns = [[(x, y) for x in range(len(line[0])) for y in range(len(line)) if line[y][x] == "#"] for line in Input]
patterns = [[pattern for pattern in patterns if len([(x, y) for x, y in pattern if y == r]) == 5] for r in [0, 6]]
locks, keys = [[[len([coord for coord in lock if coord[0] == x]) - 1 for x in range(5)] for lock in pattern] for pattern
               in patterns]

part1 = sum([min([l + k <= 5 for l, k in zip(lock, key)]) for lock in locks for key in keys])
print(part1)
