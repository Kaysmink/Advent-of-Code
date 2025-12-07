from collections import defaultdict

Input = open("data/2025/dag 07. input.txt", "r").read().split("\n")[0:-1]
splitters = {(x,y) for x in range(len(Input[0])) for y in range(len(Input)) if Input[y][x] == "^"}
max_row = max([y for x,y in splitters])
start = (Input[0].index("S"),0)


def shoot_beam(start):
    beams = {start}
    visited = defaultdict(int)
    visited[start] = 1

    step = 0
    num_splitters = 0
    while step <= max_row:
        new_beams = set()
        step = step + 1
        for x,y in beams:
            if (x,y+1) in splitters:
                num_splitters = num_splitters + 1
                visited[(x-1,y+1)] += visited[(x,y)]
                visited[(x+1,y+1)] += visited[(x,y)]
                new_beams.update([(x-1,y+1), (x+1,y+1)])
            else:
                new_beams.add((x,y+1))
                visited[(x,y+1)] += visited[(x,y)]
        beams = new_beams.copy()

    num_timelines = sum([value for (x,y), value in visited.items() if y == max_row])

    return num_splitters, num_timelines


part1, part2 = shoot_beam(start)
print(part1, part2)