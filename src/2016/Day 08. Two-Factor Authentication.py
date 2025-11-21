import re

Input = open("data/2016/dag 08. input.txt", "r").read().split("\n")[0:-1]
instructions = [re.findall(r"rect|row|column|\d+", line) for line in Input]

screen = {(x,y):False for x in range(50) for y in range(6)}

def rect(n1,n2):
    coords = [(x, y) for x in range(int(n1)) for y in range(int(n2))]
    for coord in coords:
        screen[coord] = True

def row(n1,n2):
    row_on = [x for (x, y), on in screen.items() if on and y == n1]
    new_row_on = [x+n2 if x+n2 < 50 else (x+n2)%50 if (x+n2) > 50 else 0 for x in row_on]
    new_row_off = [x for x in range(50) if x not in new_row_on]

    for x in new_row_on:
        screen[(x, n1)] = True
    for x in new_row_off:
        screen[(x, n1)] = False

def column(n1,n2):
    row_on = [y for (x, y), on in screen.items() if on and x == n1]
    new_col_on = [y+n2 if y+n2 < 6 else (y+n2)%6 if (y+n2) > 6 else 0 for y in row_on]
    new_col_off = [y for y in range(6) if y not in new_col_on]

    for y in new_col_on:
        screen[(n1, y)] = True
    for y in new_col_off:
        screen[(n1, y)] = False

def do_instructions():
    for instr, n1,n2 in instructions:
        n1, n2 = int(n1), int(n2)
        rect(n1,n2) if instr == "rect" else row(n1,n2) if instr == "row" else column(n1,n2)


def print_code():
    matrix = [["." for i in range(50)] for y in range(6)]
    on = [key for key, value in screen.items() if value]

    for (x,y) in on:
        matrix[int(y)][int(x)] = "#"

    for row in range(len(matrix)):
        print("".join(matrix[row]))

do_instructions()
part1 = sum([value for value in screen.values()])

print(part1)
print_code()
