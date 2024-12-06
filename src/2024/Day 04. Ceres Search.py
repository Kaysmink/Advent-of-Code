Input = open("data/2024/dag 04. input.txt", "r").read().split("\n")[0:-1]
Input = [list(line) for line in Input]


# Part 1
def check_xmas(x, y):
    right = "".join([Input[y][xn] for xn in [x + n for n in range(0, 4) if x + n < len(Input[0])]])
    left = "".join([Input[y][xn] for xn in [x - n for n in range(0, 4) if x - n >= 0]])
    up = "".join([Input[yn][x] for yn in [y - n for n in range(0, 4) if y - 1 >= 0]])
    down = "".join([Input[yn][x] for yn in [y + n for n in range(0, 4) if y + n < len(Input)]])

    rightdown = "".join([Input[yn][xn] for yn, xn in
                         [[y + n, x + n] for n in range(0, 4) if y + n < len(Input) and x + n < len(Input[0])]])
    rightup = "".join([Input[yn][xn] for yn, xn in
                       [[y - n, x + n] for n in range(0, 4) if y - n >= 0 and x + n < len(Input[0])]])
    leftdown = "".join([Input[yn][xn] for yn, xn in
                        [[y - n, x - n] for n in range(0, 4) if y - n >= 0 and x - n >= 0]])
    leftup = "".join([Input[yn][xn] for yn, xn in
                      [[y + n, x - n] for n in range(0, 4) if (y + n < len(Input) and x - n >= 0)]])

    alldirections = [right, left, up, down, rightdown, rightup, leftdown, leftup]

    return alldirections.count("XMAS")


part1 = sum([check_xmas(x, y) for x in range(0, len(Input[0])) for y in range(0, len(Input))])


# Part 2
def get_neighbors(x, y):
    return [Input[yn][xn] for xn in range(x - 1, x + 2) for yn in range(y - 1, y + 2) if
            0 <= xn < len(Input[0]) and 0 <= yn < len(Input) and (abs(x - xn) + abs(y - yn) in [0, 2])]


def check_x_mas(x, y):
    return "".join(get_neighbors(x, y)) in ["MMASS", "MSAMS", "SMASM", "SSAMM"]


part2 = sum([check_x_mas(x, y) for x in range(0, len(Input[0])) for y in range(0, len(Input))])

print(part1, part2)
