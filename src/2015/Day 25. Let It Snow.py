import re
import sys

sys.setrecursionlimit(3500)

yG,xG = list(map(int,re.findall(r"\d+", open("data/2015/dag 25. input.txt", "r").read())))

def get_row_start(y):
    if y in [1,2]:
        return y
    else:
        return y-1+get_row_start(y-1)


def find_location_number(x,y):
    rows_start = get_row_start(y)
    location = rows_start + sum([y+value+1 for value in range(x-1)])

    return location


def calculate_code(goal):
    value = 20151125
    for index in range(goal-1):
        value = (value * 252533) % 33554393

    return value


def code(x,y):
    location = find_location_number(x,y)
    result = calculate_code(location)

    return result

part1 = code(xG,yG)

print(part1)



