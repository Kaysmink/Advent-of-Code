from collections import defaultdict

Input = list(map(int,open("data/2017/dag 05. input.txt", "r").read().split("\n")[0:-1]))

def do_jump(jumps, part):
    index = steps = 0
    increments = defaultdict(int)
    while 0 <= index < len(jumps):
        steps = steps + 1
        jump = jumps[index]
        nx = index + jump + increments[index]
        if part == 2:
            increments[index] = increments[index] + 1 if jump + increments[index] < 3 else increments[index] - 1
        else:
            increments[index] = increments[index] + 1
        index = nx

    return steps

part1 = do_jump(Input, 1)
part2 = do_jump(Input, 2)

print(part1, part2)